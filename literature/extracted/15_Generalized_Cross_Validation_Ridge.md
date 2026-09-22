---
id: "15_Generalized_Cross_Validation_Ridge"
source_pdf: "../pdf/15_Generalized_Cross_Validation_Ridge.pdf"
source_filename: "15_Generalized_Cross_Validation_Ridge.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 108.0
visual_assets: "disabled"
---

<!-- p:1 -->

## Generalized d Cross-Validation as a Method for Choosing a Good Ridge Parameter

#### Gene H. Golub

Department of Computer Science Stanford University Stanford, CA 94303

###### Michael Heath

Computer Sciences Division Oak Ridge National Laboratory Oak Ridge, TN 37830

###### Grace Wahba

Department of Statistics University of Wisconsin Madison, WI 53705

Consider the ridge estimate β(λ) for β in the model y = Xβ + €, € ∼ N(0, σ21), σ2 unknown, β(λ) = (XTX + nλI)-1 XTy. We study the method of generalized cross-validation (GCV) for choosing a good value  for λ, from the data. The estimate λ is the minimizer of V(λ) given by

$$V ( \lambda ) = \frac { \frac { 1 } { } \left \| ( I - A ( \lambda ) ) y \right \| ^ { 2 } } { n } \Big / \left \lfloor \frac { 1 } { n } T r a c e \left ( I - A ( \lambda ) \right ) \right \rfloor ^ { 2 } ,$$

where A(λ) = X(XX + nλ/)-1XT. This estimate is a rotation-invariant version of Allen's PRESS, or ordinary cross-validation. This estimate behaves like a risk improvement estimator, but does not require an estimate of σ2, so can be used when n – p is small, or even if p ≥ n in certain cases. The GCV method can also be used in subset selection and singular value truncation methods for regression, and even to choose from among mixtures of these methods.

= (XTX)-1 XTy. (See Berger [8], Thisted [39], for recent results and references to the earlier literature.) Allowing a bias may reduce the variance tremendously.

In this paper we primarily consider the (one parameter) family of ridge estimates β(λ) given by

$$\hat { \beta } ( \lambda ) = ( X ^ { T } X + n \lambda I ) ^ { - 1 } X ^ { T } y .$$

The estimate β(λ) is the posterior mean of β if β has the prior β ∼ Q(0, aI), and λ = σ2/na. β(λ) is also the solution to the problem:

Find β which satisfies the constraint

$$\| \beta \| = \gamma$$

and for which

$$\frac { 1 } { n } \left \| y - X \beta \right \| = \min .$$

Here  ·‖ indicates the Euclidean norm and we use this norm throughout the paper. Introducing the

KEY WORDS

Ridge regression Cross-validation Ridge parameter

## 1. INTRODUCTION

Consider the standard regression model

$$y = X \beta + \epsilon \quad \quad ( 1 . 1 )$$

where y and € are column n-vectors, β is a p-vector and X is an n × p matrix; € is random with Ee = 0, Eεe = σ2I, where I is the n × n identity.

For p ≥ 3, it is known that there exist estimates of β with smaller mean square error than the minimum variance unbiased, or Gauss-Markov, estimate β(0) 11 n

Received June 1977; revised April 1978


<!-- p:2 -->


Lagrangian we find that the above problem is equivalent to finding the minimum over β of

$$\frac { 1 } { n } \left \| y - X \beta \right \| ^ { 2 } + \lambda \left \| \beta \right \| ^ { 2 } & & ( 1 , 3 ) \\$$

where λ is a Lagrange multiplier. Methods for computing λ given γ are given in [17]. See [29] for discussion of (1.3). The method of minimizing equation (1.3), or its Hilbert space generalizations, is called the method of regularization in the approximation theory literature (see [21, 44] for further references).

It is known that for any problem there is a λ &gt; 0 for which the expected mean square error Eβ - β(λ) l 2 is less than the Gauss-Markov estimate; however the λ which minimizes, say Elβ - β(λ)∥, or any other given nontrivial quadratic loss function depends on σ2 and the unknown β.

There has been a substantial amount of interest in estimating a good value of λ from the data. See [10, 11, 12, 15, 20, 22, 23, 25, 26, 27, 30, 31, 32, 35, 38, 39]. A conservative guess might put the number of published estimates for λ at several dozen.

In this paper we examine the properties of the method of generalized cross-validation (GCV) for obtaining a good estimate of λ from the data. The GCV estimate of λ in the ridge estimate (1.2) is the minimizer of V(λ) given by

$$V ( \lambda ) = \frac { 1 } { n } \left \| ( I - A ( \lambda ) y \right \| ^ { 2 } / \left [ \frac { 1 } { n } \, T r a c \left ( I - A ( \lambda ) \right ) \right ] ^ { 2 } , \quad \text {there} \quad \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \$$

where

$$A ( \lambda ) = X ( X ^ { T } X + n \lambda J ) ^ { - 1 } X ^ { T } . \quad ( 1 . 5 ) \quad \underset { \substack { n u \\ n u } } { \text {mul} }$$

A discussion of the source of V(λ) will be given in Section 2. This estimate is a rotation-invariant version of Allen's PRESS or ordinary cross-validation, as described in Hocking's discussion to Stone's paper [36] (see also Allen [3], and Geisser [13]). A discussion of the source of V(λ) will be given in Section 2. This estimate is a rotation-invariant version of Allen's PRESS or ordinary cross-validation, as described in Hocking's discussion to Stone's paper [36] (see also Allen [3], and Geisser [13]).

Let T(λ) be the mean square error in estimating Xβ, that is, Let T(λ) be the mean square error in estimating Xβ, that is,

$$\mathcal { T } ( \lambda ) = \frac { 1 } { n } \ \| X \beta - X \hat { \beta } ( \lambda ) \| ^ { 2 } . \quad ( 1 . 6 )$$

It is straightforward to show that It is straightforward to show that

$$E T ( \lambda ) = \frac { 1 } { n } \| ( I - A ( \lambda ) ) g \| ^ { 2 } + \frac { \sigma ^ { 2 } } { n } T r \, A ^ { 2 } ( \lambda ) \quad ( 1 . 7 )$$

where where

$$g = X \beta .$$

An unbiased estimator (λ) of ET(λ), for n &gt; p, is given by An unbiased estimator T(λ) of ET(λ), for n &gt; p, is given by

$$\hat { T } ( \lambda ) = \frac { 1 } { n } \left \| ( I - A ( \lambda ) ) y \right \| ^ { 2 } - \frac { 2 \hat { \sigma } ^ { 2 } } { n } T r ( I - A ( \lambda ) ) + \hat { \sigma } ^ { 2 } , \\$$

where

$$\hat { \sigma } ^ { 2 } = \frac { 1 } { n - p } \, \| ( I - X ( X ^ { T } X ) ^ { - 1 } X ^ { T } ) y \| ^ { 2 } .$$

Mallows [28, p. 672] has suggested choosing λ to minimize Mallows' CL, which is equivalent to minimizing n T(λ)/2. (This follows from [28] upon noting that (I - A(λ))y2 is the "residual sum of squares.") The minimizer of T was also suggested by Hudson [25]. We shall call an estimate formed by minimizing T an RR ("range risk") estimate.

We shall show that the GCV estimate is, for large n, an estimate for the λ which approximately minimizes ET(λ) of (1.7), without the necessity of estimating σ2. As a consequence of not needing an estimate of σ2, GCV can be used on problems where n − p is small, or (in certain circumstances), where the "real" model may be

$$y _ { \iota } = \sum _ { j = 1 } ^ { \infty } \ x _ { \iota } \beta _ { j } + \epsilon _ { \iota } , \quad i = 1 , 2 , \cdots , n . \ ( 1 . 9 )$$

It is also natural for solving regression-like problems that come from an attempt to solve ill-posed linear operator equations numerically. In these problems there is typically no way of estimating σ2 from the data. See Hanson [19], Hilgers [21], Varah [40] for descriptions of these problems. See Wahba [44] for the use of GCV in estimating λ in the context of ridge-type approximate solutions for ill-posed linear operator equations, and for further references to the numerical analysis literature. See Wahba, Wahba and Wold, and Craven and Wahba [9, 42, 43, 45, 46] for the use of GCV for curve smoothing, numerical dif ferentiation, and the optimal smoothing of density and spectral density estimates. At the time of this writing, the only other methods we know of for estimating λ from the data without either knowledge of or an estimate of σ2, are PRESS and maximum likelihood, to be described. We shall indicate why GCV can be expected to be generally better than either. (PRESS and GCV will coincide if XXT is a circulant matrix.)

A fundamental tool in our analysis and in our computations is the singular value decomposition. Given any n × p matrix X, we may write

$$X = U D V ^ { T }$$

where U is an n × n orthogonal matrix, V is a p ×p orthogonal matrix, and D is an n ×p diagonal matrix whose entries are the square roots of the eigenvalues of XaX. The number of non-zero entries in D is equal to the rank of X. The singular value decomposition arises in a number of statistical applications [18]. Good numerical procedures are given in [16].


<!-- p:3 -->


In Section 2 we derive the GCV estimate as a rotation-invariant version of Allen's PRESS and discuss why it should be generally superior to PRESS. In Section 3 we give some theorems concerning its properties. In Section 4 we show how GCV can be used in other regression procedures, namely, subset selection, and eigenvalue truncation, or principal components. Indeed GCV can be used to compare between the best of the three different methods, or mixtures, of them, if you will. In Section 5 we present the results of a Monte Carlo example.

## 2. THE GENERALIZED CROSS-VALIDATION ESTIMATE OF λ AS AN INVARIANT VERSION OF ALLEN'S PRESS

The Allen's PRESS, or ordinary cross-validation estimate of λ, goes as follows. Let β()(λ) be the ridge estimate (1.2) of β with the kth data point y', omitted. The argument is that if λ is a good choice, then the kth component [Xβ(k)(λ)]k of Xβ(k)(λ) should be a good predictor of y. Therefore, the Allen's PRESS estimate of λ is the minimizer of

$$P ( \lambda ) = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left ( [ X \beta ^ { ( k ) } ( \lambda ) ] _ { k } - y _ { k } \right ) ^ { 2 } . \quad ( 2 . 1 ) \quad \begin{matrix} \text {circuit} \\ \text {nail} \\ \text {is } \end{matrix}$$

It has been observed by one of the referees that P(λ) may be viewed as a direct sample estimate of kEy+∥y* − Xβ(λ)||2 ≡ T(λ) + σ2, where here β(λ) is supposed fixed, y* is a future hypothetical observation vector, and Ey· denotes expectation over the distribution of y*.

It can be shown, by use of the Sherman-MorrisonWoodbury formula (see [24]), that

$$P ( \lambda ) = \frac { 1 } { n } \left \| B ( \lambda ) ( I - A ) \right ) y \right \| ^ { 2 } ,$$

where B(λ) is the diagonal matrix with jjth entry 1/(1 − a(λ)), a,(λ) being the jjth entry of A(λ) = X(XTX + nλI)−1XT.

Although the idea of PRESS is intuitively appealing, it can be seen that in the extreme case where the entries of X are 0 except for x, i = 1, 2, · · ·, p, then [Xβ()(λ)] cannot be expected to be a good predictor of yk. In fact, in this case A(λ) is diagonal.

$$P ( \lambda ) = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \, y _ { k } \, ^ { 2 } ,$$

and so P(λ) does not have a unique minimizer. It is reasonable to conclude that PRESS would not do very well in the near diagonal case. If β and ε both have spherical normal priors, then various arguments can be brought to bear that any good estimate of λ should be invariant under rotations of the (measurement) coordinate system. The GCV estimate is a rotation-invariant form of ordinary cross-validation. It may be derived as follows: Let the singular value decomposition [16] of X be

$$X = U D V ^ { t } .$$

Let W be the unitary matrix which diagonalizes the circulants. (See Bellman [7], Wahba [41].) In complex form the jkth entry [W] of W is

$$[ W ] _ { k } = \frac { 1 } { \sqrt { n } } \, e ^ { 2 \pi i j k / n } , \quad j , k = 1 , 2 , \cdots , n .$$

The GCV estimate for λ can be defined as the result of using Allen's PRESS on the transformed model

$$\tilde { y } = W U ^ { \tau } y = W D V ^ { \tau } \beta + W U ^ { \tau } \epsilon \\ \equiv \chi _ { \beta } + W U ^ { \tau } \epsilon .$$

The new "data vector" is y = (1, ·  , yn), and the m   a = X   , ans complex conjugate transpose) is a circulant matrix (see [6,41]). Thus intuitively, [Xβ(k)(λ)] should contain a "maximal" amount of information about yk, on the average. By substituting X and y into (2.2), and observing that A(λ) ≡ X(X*X + nλI)−1X* is a circulant matrix and hence constant down the diagonals, and Ā(λ) and A(λ) have the same eigenvalues, it is seen that P(λ) becomes V(λ) (see (1.4)) given by

$$t \text { that } & \quad \text {is seen that } P ( \lambda ) \text { becomes } V ( \lambda ) \text { (see (1.4)) } \text { given by } \\ \text {te of } & \quad V ( \lambda ) = \frac { 1 } { n } \left \| ( I - \tilde { A } ( \lambda ) ) \tilde { y } \right \| ^ { 2 } \Big / \\ \text {erva- } & \quad \text {the } & \quad \left [ \frac { 1 } { n } \text { Tr} ( I - \tilde { A } ( \lambda ) ) \right ] ^ { 2 } \\ \text {ison-} & \quad & \equiv \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \left ( \frac { n \lambda } { \lambda _ { \nu n } + n \lambda } \right ) ^ { 2 } z _ { \nu } ^ { 2 } \Big / \\ ( 2 . 2 ) & & \left [ \frac { 1 } { n } \sum _ { \nu = 1 } ^ { p } \frac { n \lambda } { \lambda _ { \nu n } + n \lambda } + n - p \right ] ^ { 2 } & ( 2 . 3 ) \\ & 1 / ( 1 \\ ( X ^ { T } X \quad \text {where } z = ( z _ { \nu } , \cdots , z _ { n } ) ^ { T } = H ^ { T } v \text { and } \lambda _ { \nu } = 1 , 2 , \cdots , n$$

where z = (z1, · · ·, zn)T = UT y and λvn, ν = 1, 2, · · · , n, are the eigenvalues of XXT, λ = 0, ν &gt; p.

It can also be shown that V(λ) is a weighted version of P(λ), namely

$$V ( \lambda ) \equiv \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left ( [ X \beta ^ { ( k ) } ( \lambda ) ] _ { k } - y _ { k } \right ) ^ { 2 } w _ { k } ^ { ( \lambda ) }$$

where

$$w _ { \kappa } ( \lambda ) = \frac { 1 - a _ { \kappa \kappa } ( \lambda ) } { 1 - \frac { 1 } { n } T r \, A ( \lambda ) } \cdot$$

We define the GCV estimate of λ as the minimizer of (1.4), equivalently (2.3), and proceed to an investigation of its properties. We define the GCV estimate of λ as the minimizer of (1.4), equivalently (2.3), and proceed to an investigation of its properties.


<!-- p:4 -->


3. PROPERTIES OF THE GCV ESTIMATE OF λ

satisfies

Theorem 1 (The GCV Theorem).

$$\left | T r ( A ( \lambda ) , \mu _ { 2 } = \frac { 1 } { n } \, T r \, A ^ { z } ( \lambda ) , \, b ^ { 2 } = \\ & \frac { 1 } { n } \left \| ( I - A ( \lambda ) ) g \right \| ^ { z } . \quad \text {are} \\$$

Then

$$\frac { E T ( \lambda ) - E V ( \lambda ) + \sigma ^ { 2 } } { E T ( \lambda ) } & = \frac { - \mu _ { 1 } ( 2 - \mu _ { 1 } ) } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \\ & + \frac { \sigma ^ { 2 } } { b ^ { 2 } + \sigma ^ { 2 } \mu _ { 2 } } \frac { \mu _ { 1 } ^ { 2 } } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \\$$

and so

$$\frac { | E T ( \lambda ) - E V ( \lambda ) + \sigma ^ { 2 } | } { E T ( \lambda ) } < \left ( 2 \mu _ { 1 } + \frac { \mu _ { 1 } ^ { 2 } } { \mu _ { 2 } } \right ) \frac { 1 } { ( 1 - \mu _ { 1 } ) ^ { 2 } }$$

whenever 0 &lt; μ1 &lt; 1. Proof: Since ET = b2 + σ2μ22 EV = [b2 + σ2(1 − 2μ1 + μz)]/(1 − μ)2, the result follows from

$$\mu _ { 2 } ) ] / ( 1 - \mu _ { 1 } ) ^ { 2 } , \, \text { the result follows from} \\ E T - E V = ( b ^ { 2 } + \sigma ^ { 2 } \mu _ { 2 } ) \left ( 1 - \frac { 1 } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \right ) & & \text {and and so} \\ & & - \sigma ^ { 2 } \frac { ( 1 - 2 \mu _ { 1 } ) } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \\ E T + \sigma ^ { 2 } - E V = E T \left ( 1 - \frac { 1 } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \right ) + \sigma ^ { 2 } \frac { \mu _ { 1 } ^ { 2 } } { ( 1 - \mu _ { 1 } ) ^ { 2 } } & & \text {If $\Lambda$} \\ R e m a r k \colon \text {This theorem implies that if}$$

Remark: This theorem implies that if

$$\frac { 1 } { n } \, T r \, A ( \lambda ) = \mu _ { 1 } \rightarrow 0 & & \text {as } n \rightarrow \infty$$

$$I ^ { o } \leq \frac { 1 + h ( \lambda ^ { o } ) } { 1 - h ( \tilde { \lambda } ) } \, .$$

Remark: This corollary sa are small then the mean squa of EV(λ) is not much bigger sible mean square error mir Remark: This corollary says that if h(λo) and h(λ) are small then the mean square error at the minimizer of EV(λ) is not much bigger than the minimum possible mean square error min ET(λ).

Proof: Let Λ = {λ: 0 ≤ (λ°)(1 + h(λ°))}. Since Proof: Let Λ = {λ: 0 ≤ λ ≤ ∞, EV(λ) − σ2 ≤ T(λ°)(1 + h(λ°))}. Since

$$E T ( \lambda ) ( 1 - h ( \lambda ) ) & < E V ( \lambda ) - \sigma ^ { 2 } < E T ( \lambda ) ( 1 + h ( \lambda ) ) , \\ 0 & \leq \lambda < \infty ,$$

and ET, EV and h are contin Λ is a non-empty closed set point of Λ, then EV(λ) − σ2 h in the interior of Λ, call it λ. the theorem and ET, EV and h are continuous functions of λ, then Λ is a non-empty closed set. If 0 is not a boundary point of Λ, then EV(λ) − σ2 has at least one minimum in the interior of Λ, call it λ. (See Figure 1.) Now by the theorem

ET()(1 − h()) &lt; EV() − and so ET(λ)(1 − h(λ)) &lt; EV(λ) − σ2 &lt; ET(λ°)(1 + h(λ°)) and so

$$I ^ { 0 } = \frac { T ( \tilde { \lambda } ) } { T ( \lambda ^ { 0 } ) } \leq \frac { 1 + h ( \lambda ^ { 0 } ) } { 1 - h ( \lambda ) } .$$

If Λ includes 0, then λ may b i.e., λ = 0, but the above bo Example 1. Note that If Λ includes 0, then λ may be on the boundary of Λ, i.e., λ = 0, but the above bound on Io still holds. Example 1. Note that

$$\mu _ { 1 } = \frac { 1 } { n } \, T r \, A = \frac { 1 } { n } \sum _ { \nu = 1 } ^ { p } \, \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + n \lambda } \leq \frac { p } { n }$$

and

$$\left ( \frac { 1 } { n } \ T r \, A ( \lambda ) \right ) ^ { 2 } / \left ( \frac { 1 } { n } \ T r \, A ^ { 2 } ( \lambda ) \right ) & = \frac { \mu _ { 1 } ^ { 2 } } { \mu _ { 2 } } \rightarrow 0 . \quad \text {as } n \rightarrow \infty \\$$

then the difference between ET(λ) + σ2 and EV(λ) is small compared to ET(λ). This result and the fact that in the extreme diagonal case P(λ) does not have a unique minimum suggests that the minimizer of V(λ) is preferable to the minimizer of P(λ) if one wants to choose λ to minimize

$$\frac { 1 } { n } \, E _ { y ^ { * } } \| y ^ { * } - X \beta ( \lambda ) \| ^ { 2 } .$$

Corollary: Let

$$h = \left ( 2 \mu _ { 1 } + \frac { \mu _ { 1 } ^ { 2 } } { \mu _ { 2 } } \right ) \frac { 1 } { ( 1 - \mu _ { 1 } ) ^ { 2 } }$$

Let λo be the minimizer of ET(λ). Then EV(λ) always -as     mo ( l sl  e pectation inefficiency" Io defined by

$$I ^ { o } = \frac { E T ( \tilde { \lambda } ) } { E T ( \lambda ^ { o } ) }$$

TECHNOMETRICS ©, VOL. 21, NO. 2, MAY 1979

$$\frac { \mu _ { 1 } ^ { 2 } } { \mu _ { 2 } } = \frac { \left ( \frac { 1 } { n } \, T r \, A \right ) ^ { 2 } } { \frac { 1 } { n } \, T r \, A ^ { 2 } } = \frac { 1 } { n } \, \frac { \left ( \sum _ { \nu = 1 } ^ { p } \, \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + \lambda } \right ) ^ { 2 } } { \sum _ { \nu = 1 } ^ { p } \left ( \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + \lambda } \right ) ^ { 2 } } \leq \frac { p } { n } .$$

Then Then

$$h \leq 3 \, \frac { P } { n } \, \frac { 1 } { \left ( 1 - \frac { P } { n } \right ) ^ { 2 } } \, .$$

Hence for p fixed and n → that Hence for p fixed and n → ∞, it follows that

$$I ^ { \circ } \leq 1 + 6 \, \frac { P } { n } + 0 \left ( \frac { P } { n } \right ) .$$

Example 2. p &gt; n. Example 2. p &gt; n.

It is not necessary that p this example suggests. Wha become ill conditioned for It is not necessary that p &lt;&lt; n for Io to tend to 1, as this example suggests. What is required is that XXT become ill conditioned for n large.


<!-- p:5 -->


Let

with

$$\sum _ { l = 1 } ^ { \infty } x _ { l } x _ { l } ^ { 2 } \leq k _ { 1 } < \infty , \ \ a l ] \quad i , \quad \sum _ { l = 1 } ^ { \infty } \beta _ { j } ^ { 2 } \leq k _ { 2 } < \infty .$$

Suppose

$$\lim _ { n \to \infty } \frac { 1 } { n } \, T r \, X X ^ { T } = \lim _ { n \to \infty } \frac { 1 } { n } \sum _ { l = 1 } ^ { n } \, \sum _ { J = 1 } ^ { \infty } \, x _ { l J } { ^ { 2 } } = k _ { \mathfrak { s } } < \infty$$

and suppose the eigenvalues {λvn, ν = 1, 2, · · · , n} of XXT satisfy

$$\lambda _ { \nu n } \simeq n \nu ^ { - m } ,$$

8 say, for some m &gt; 1; (ks = ∑ v−m). 1=4

Then

$$T h e n \\ \mu _ { 1 } = \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + n \lambda } \simeq \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { 1 + \lambda \nu ^ { m } } \sum _ { \substack { P r o o \\ E _ { \beta } E _ { \beta } } } ^ { \substack { m i z e c h o l l \\ m i z e c h o l l } } \\ \simeq \frac { 1 } { n } \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + \lambda x ^ { m } ) } = \frac { 1 } { n \lambda ^ { 1 / m } } \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + x ^ { m } ) } \\ E _ { \beta } E _ { \beta } \\ \mu _ { 2 } = \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \left ( \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + n \lambda } \right ) ^ { 2 } \simeq \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \lambda \nu ^ { m } ) ^ { 2 } } \\ \simeq \frac { 1 } { n } \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + \lambda x ^ { m } ) ^ { 2 } } = \frac { 1 } { n \lambda ^ { 1 / m } } \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + x ^ { m } ) ^ { 2 } } . \\ \intertext { a n d } \mu _ { 1 } \rightarrow 0 , \, \mu _ { 1 } ^ { 2 } / \mu _ { 2 } \rightarrow 0 \quad \text {if} \quad n \lambda ^ { 1 / m } \rightarrow \infty .$$

and μ1 → 0, μ12/μ2 → 0 if nλ1/m →∞. Now

b2(λ) = λ βT(XTX + nλI)−1(nλ)XTX(XTX + nλI)−1β

$$\leq \frac { \lambda } { 2 } \left \| \beta \right \| ^ { 2 } \leq \frac { \lambda } { 2 } \, k _ { 2 } ,$$

FIGURE 1. Graphical suggestion of the proof of the corollary to the GCV theorem.

### Theorem 2. Theorem 2.

Proof: Since Eg gT = E XββTXT = a XXT, Proof: Since Eg gT = E XββXT = a XXT,

The minimizer of EβEV(λ) is the same as the minimizer of EβET(λ) and is λ = σ2/na. The minimizer of EβEV(λ) is the same as the minimizer of EβET(λ) and is λ = σ2/na.

02

$$E _ { \beta } E T ( \lambda ) & = \frac { \alpha } { n } \, T r \left ( I - A \right ) ^ { 2 } X X ^ { T } + \frac { \sigma ^ { 2 } } { n } \, T r \, A ^ { 2 } \\ E _ { \beta } E V ( \lambda ) & \equiv \left [ \frac { \alpha } { n } \, T r \left ( I - A \right ) ^ { 2 } X X ^ { T } + \frac { \sigma ^ { 2 } } { n } \, T r \, ( I - A ) ^ { 2 } \right ] \\ & / \left [ \frac { 1 } { n } \, T r \left ( I - A \right ) \right ] ^ { 2 } . \quad ( 3 . 3 ) \\ \text {The proof proceeds by differentiating} \, ( 3 . 3 ) \text { with } r \in \real .$$

The proof proceeds by differentiating (3.3) with respect to λ and setting the remainder equal to 0. This calculation has appeared elsewhere [43 p. 8], and will be omitted. The proof proceeds by differentiating (3.3) with respect to λ and setting the remainder equal to 0. This calculation has appeared elsewhere [43 p. 8], and will be omitted.

## 4. GCV IN SUBSET SELECTION AND GENERAL LINEAR MODEL BUILDING 4. GCV IN SUBSET SELECTION AND GENERAL LINEAR MODEL BUILDING

since the largest eigenvalue of

(XTX + nλI)−1(nλ)XTX(XTX + nλI)−1

$$= \max _ { \nu } \frac { ( \lambda _ { \nu n } ) ( n \lambda ) } { ( \lambda _ { \nu n } ) ^ { 2 } + ( n \lambda ) ^ { 2 } } \leq \frac { 1 } { 2 } \cdot$$

As n → ∞, the minimizing sequence λ° = λ(n) of ET(λ) = b2(λ) + σ2μz(λ) clearly must satisfy λ° → 0, n(λ°)i/m → ∞, so that the GCV Theorem may be applied. It is proved in [9, 44] in a different context that λ as well as λo satisfies (nλi/m) → ∞ so that h(λ) → 0, h(λ°) → 0 and Io ↓ 1 as n → ∞.

Instead of viewing β as fixed but unknown, suppose that β has the prior β ∼ N(0, aI). Let Eβ be expectation with respect to the prior. (We reserve E for expectation with respect to €.) Then Let y = g + €, where g is a fixed (unknown) nvector and € ∼ N(0, σ2I), σ2 unknown. Let A(ν), ν in some index set, be a family of symmetric nonnegative definite n × n matrices and let Let y = g + €, where g is a fixed (unknown) nvector and ε ∼ N(0, σ2I), σ2 unknown. Let A(ν), ν in some index set, be a family of symmetric nonnegative definite n ×n matrices and let

$$\underline { 1 }$$

$$n$$

$$\mu _ { 1 } ( \nu ) & = \frac { 1 } { n } \, T r \, A ( \nu ) \\ \mu _ { z } ( \nu ) & = \frac { 1 } { n } \, T r \, A ^ { 2 } ( \nu ) .$$

Letting Letting

$$T ( \nu ) \simeq \frac { 1 } { n } \left \| \ g - A ( \nu ) y \right \| ^ { 2 }$$

and V(ν) as before with A(λ) replaced by A(ν), then (3.1) clearly holds irrespective of the nature of A. and V(ν) as before with A(λ) replaced by A(ν), then (3.1) clearly holds irrespective of the nature of A.

A different way of dealing with ill conditioning in A different way of dealing with ill conditioning in

$$y _ { \iota } = \sum _ { J = 1 } ^ { p } x _ { \iota J } \beta _ { J } + \epsilon _ { \iota } , \quad i = 1 , 2 , \cdots , \\ p > n$$


<!-- p:6 -->


the design matrix is to reduce the number of predictor variables by choosing a subset β, β   , β of the β's. Let v be an index on the 2a possible subsets of β1, , βp let X(TM) be the n × k(ν) design matrix corresponding to the yth subset, and let

$$\hat { \beta } ( \nu ) & = ( X ^ { ( \nu ) \mathcal { T } } X ^ { ( \nu ) } ) ^ { - 1 } X ^ { ( \nu ) } y \\ A ( \nu ) & = \ X ^ { ( \nu ) } ( X ^ { ( \nu ) \mathcal { T } } X ^ { ( \nu ) } ) X ^ { ( \nu ) } y .$$

Then Then

$$\mu _ { 1 } = \, k / n , \quad \mu _ { 1 } ^ { 2 } / \mu _ { 2 } = k / n .$$

Mallows [28] suggestion to choose the subset minimizing Cp becomes, in our notation, the equivalent of minimizing (·) of (1.8) with A(λ) replaced by A(ν), see also Allen [2]. This assumes that an estimate of σ2 is available. Parzen [33] has observed that, if one prefers to choose a subset without estimating σ2, (because one believed in the model (3.2), say), GCV can be used. The subset of size ≤ kmax with smallest V can be chosen, knowing that

$$\left | \frac { E T ( \nu ) - E V ( \nu ) - \sigma ^ { x } } { E T ( \nu ) } \left \{ \leq \frac { k _ { \max } } { n } \ ,$$

even if the model (3.2) is nontrivially true.

In the subset selection case, GCV asymptotically coincides with the use of Akaike's information criterion AIC [1] since

$$A I C & = ( - 2 ) \log \max i l i h o o d + 2 k \\ & = n \log \frac { 1 } { n } \left \| ( I - A ) y \right \| ^ { 2 } + 2 k$$

and so

$$\text { and so } & & \text { and so } & & \frac { 1 } { n } \left \| ( I - A ) y \right \| ^ { 2 } & \frac { 1 } { n } \left \| ( I - A ) y \right \| ^ { 2 } \\ e ^ { A I C / n } & = \frac { \frac { 1 } { n } } { \left ( e - \frac { k } { n } \right ) ^ { 2 } } \approx \frac { \frac { 1 } { n } } { \left ( 1 - \frac { k } { n } \right ) ^ { 2 } } = V \\ & \text { as } & & \frac { k } { n } \rightarrow 0 .$$

$$n$$

We thank E. Parzen for pointing this out. M. Stone, [37] has investigated the relations between AIC and (ordinary) cross-validation.

Another approach, the principal components approach, is also popular in solving ill-posed linear operator equations, see Baker et al. [6], Hanson [19], Varah [40]). The method is to replace X by X(ν) defined by X(v) = U D(ν) VT, where D(ν) is the diagonal matrix of singular values of V with all but the yth subset of singular values set equal to 0. Then

$$\begin{array} { r l } { \bar { \ } n u s b s e t o r s i g u a r v a r s e t e q u a r t i o n t o r . T h e n } \\ { A ( \nu ) = U \ D ( \nu ) \left ( D ( \nu ) D ( \nu ) ^ { T } \right ) ^ { + } \ D ( \nu ) \ U ^ { T } } \\ { = U \left ( \begin{matrix} 1 & \cdot & 0 \\ & & 1 \\ & & 0 \\ 0 & & 0 \end{matrix} \right ) \ U ^ { T } } \\ { \bar { \ } n u s b s e t o r s i g u a r v a r s e t e q u a r t i o n t o r . } \end{array}$$

TECHNOMETRICS ©, VOL. 21, NO. 2, MAY 1979

where the ones are located at positions of the th subset of singular values, and, again μ1 ≤ p/n, μ2/μ2 ≤ p/n, where p can be replaced by the number of singular values in the largest subset considered.

In fact, it is reasonable to select from among any family {A(v)} of matrices for which the corresponding μ1 and μ2/μ2 are uniformly small, by choosing that member for which V(v) is smallest. Mixtures of the above methods, e.g. a ridge method on a subset, can be handled this way. Note that the conditions μ small, μ12/μ2 small are just those conditions which make it plausible that the "signal"g can be separated from the noise. These conditions say that the A matrix essentially maps the data vector (roughly) into some much smaller subspace than the whole space. Parzen [34] has also indicated how GCV can be used to choose the order of an autoregressive model to fit a stationary time series.

## 5. A NUMERICAL EXAMPLE

We choose a discretization of the Laplace transform as given in Varah, [40, p. 262] as an example in which XaX is very ill conditioned.

We emphasize that the following is nothing more than a single example, with a single X and β. It does not indicate what may happen as X and β are varied. It is intended as an indication of the type of Monte Carlo evaluation study that an experimenter might perform with the particular X that he has at hand, and perhaps one or several β that represent the class of β's he believes he is likely to encounter. We suggest that an experimenter with particular design matrix at hand evaluate candidate methods (at least crudely), components, as well as ridge methods against his X perhaps including subset selection and/or principal and against a realistic set of β, before final selection of a method. The values for n and p in the experiment presented here were 21 and 10 and the condition number of X, namely the ratio of the largest to the smallest (non-zero) singular value, was 1.54 × 105. The value of Xβ||  was 370.84.

Four values of σ2, namely σ2 = 10−8, 10−6, 10−4 and 10-2 were tried and for each value of σ2 the experiment was replicated four times, giving a total of 16 runs. The € were generated as pseudo-random 0, σ2) independent r.v.'s, V(λ) was computed using the right-hand side of (2.3) and the Golub-Reinsch singular value decomposition [16]. The minimizer  of V(λ) was determined by a global search. T(λ) was also computed and the relative inefficiencies fp and f of λ defined by

$$I _ { D } & = \ \| \beta - \beta _ { \lambda } \| ^ { 2 } / ( \min _ { \lambda } \ \| \beta - \hat { \beta } _ { \lambda } \| ^ { 2 } ) \\ I _ { R } & = \ T ( \hat { \lambda } ) / \min _ { \lambda } T ( \lambda )$$

were computed. (D = "domain", R = "range.")


<!-- p:7 -->


TABLE 1—Observed inefficiencies in sixteen Monte Carlo runs.

|                       | Replication 1 - ID    | Replication 1 - IR    | Replication 2 - ID    | Replication 2 - R     | Replication 3 - ID    | Replication 3 - IR    | Replication 4 - ID    | Replication 4 - IR    |
|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 | cr2=10 -8, S/N = 4200 |
| GCV                   | 4.43                  | 1.06                  | 1.65                  | 1.03                  | 16.71                 | 1.10                  | 1.02                  | 1.01                  |
| RR                    | 1.46                  | 1.00                  | 1.66                  | 1.03                  | 8.69                  | 1.01                  | 1.22                  | 1.03                  |
| MLE                   | 1.67E3                | 1.31                  | 1.45E2                | 1.23                  | 2.00E3                | 1.53                  | 9.12E3                | 1.51                  |
| PRESS                 | 2.31E3                | 4.8E4                 | 6.31E2                | 8.6E4                 | 3.84E3                | 2.1E5                 | 2.87E3                | 1.2E5                 |
| Min Sol'n             | 1.00                  | 1.02                  | 1.00                  | 1.54                  | 1.00                  | 2.27                  | 1.00                  | 1.00                  |
| Min Data              | 1.20                  | 1.00                  | 2.89                  | 1.00                  | 5.97                  | 1.00                  | 1.00                  | 1.00                  |
| a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   | a2=10 -6, S/N = 420   |
| GCV                   | 1.92                  | 1.05                  | 1.32                  | 1.00                  | 1.51E2                | 1.26                  | 2.20                  | 1.02                  |
| RR                    | 1.83                  | 1.06                  | 1.90                  | 1.01                  | 7.03El                | 1.10                  | 1.18                  | 1.00                  |
| MLE                   | 1.99E2                | 1.19                  | 1.70E2                | 1.45                  | 1.76E2                | 1.29                  | 1.49E2                | 1.32                  |
| PRESS                 | 5.80                  | 1.01                  | 2.41E2                | 1.39E4                | 36.37                 | 2.43E3                | 67.00                 | 6.07E2                |
| Min Sol'n             | 1.00                  | 1.38                  | 1.00                  | 1.02                  | 1.00                  | 1.20                  | 1.00                  | 1.03                  |
| Min Data              | 3.56                  | 1.00                  | 1.28                  | 1.00                  | 7.85                  | 1.00                  | 41.29                 | 1.00                  |
| 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     | 02=10-4, S/N = 42     |
| GCV                   | 1.27                  | 1.07                  | 1.50                  | 2.58                  | 1.00                  | 1.11                  | 1.00                  | 1.03                  |
| RR                    | 1.18                  | 1.08                  | 1.03                  | 2.27                  | 1.07                  | 1.13                  | 1.00                  | 1.03                  |
| MLE                   | 1.56                  | 1.20                  | 12.16                 | 3.43                  | 1.90                  | 1.49                  | 2.97                  | 1.07                  |
| PRESS                 | 3.53                  | 1.57                  | 2.03                  | 3.43                  | 8.66                  | 2.63                  | 2.90                  | 24.34                 |
| Min Sol'n             | 1.00                  | 1.21                  | 1.00                  | 2.05                  | 1.00                  | 1.11                  | 1.00                  | 1.03                  |
| Min Data              | 3.26                  | 1.00                  | 1.16                  | 1.00                  | 2.39                  | 1.00                  | 1.16                  | 1.00                  |
| 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   | 02=10 -2, S/N z 4.2   |
| GCV                   | 1.40                  | 2.47                  | 2.01                  | 1.60                  | 1.59                  | 1.01                  | 31.20                 | 17.2                  |
| XR                    | 1.38                  | 2.39                  | 2.41                  | 1.70                  | 1.41                  | 1.02                  | 10.8                  | 10.6                  |
| MLE                   | 2.13                  | 3.56                  | 3.81                  | 1.87                  | 2.00                  | 1.00                  | 28.8                  | 16.8                  |
| PRESS                 | 1.04                  | 1.01                  | 2.02                  | 2.68                  | 1.00                  | 1.22                  | 2.16                  | 21.5                  |
| Min Sol'n             | 1.00                  | 1.31                  | 1.00                  | 1.01                  | 1.00                  | 1.25                  | 1.00                  | 1.98                  |
| Min Data              | 1.02                  | 1.00                  | 1.00                  | 1.00                  | 2.66                  | 1.00                  | 1.21                  | 1.00                  |

The results of a comparison with three other methods are also presented. The methods are, respectively,

2. Range risk, (RR) the minimizer of Î(λ).
1. PRESS, the minimizer of P(λ).
3. Maximum likelihood (MLE).

The maximum likelihood estimate is obtained from the model

$$y = X \beta + \epsilon$$

with ε ~ X(0, σ2I) and β having the prior distribution β~ X0, al). Then the posterior distribution of y is

$$y \sim N ( 0 , a ( X X ^ { T } + n \lambda I ) ) \quad ( 5 . 2 ) \quad t h$$

where λ = σ2/na. The ML estimate for λ from the model (5.2) is then the minimizer of M(λ) given by

$$M ( \lambda ) = \frac { 1 } { n } \, \frac { y ^ { r } ( I - A ( \lambda ) ) y } { [ \det ( I - A ( \lambda ) ) ] ^ { 1 / n } } \cdot \quad ( 5 . 3 ) \quad \begin{matrix} \text {res} \\ \text {fin} \end{matrix}$$

This estimate is the general form of the maximum likelihood estimate suggested by Anderssen and Bloomfield in the context of numerical differentiation [4,5]. It can be shown that the minimizer of Eβ E M(λ) is σ2/na. However, it can also be shown that if β behaves as though it did not come from the prior

$$\left ( e . g . \text { as in the model } ( 1 . 9 ) , \ \sum _ { i = 1 } ^ { \infty } \beta _ { i } ^ { 2 } < \infty \right )$$

then the minimizer of E M(λ) may not be a good estimate of the minimizer of ER(λ).

Ip and IR of (5.1) were determined for each of these three methods as well as GCV and the results are presented in Table 1. The entries next to "Min Sol'n" and "Min Data" are the inefficiencies (5.1) with λ replaced by the minimizers of β-β and T(λ) respectively. S/N, the "signal to noise ratio" is defined by S/N = [1/n∥Xβ∥2/σ2]1/2 Figure 2 gives a

$$T E C H N O M E T R I C S \ \mathcal { O } , \, V O L . \, 2 1 , \, N O . \, 2 , \, M A Y \, 1 9 7 9$$


<!-- p:8 -->


FIGURE 2. V(λ), T(λ), f(λ), M(λ), P(λ) and ∥β−βλ||2.

plot of V(λ), T(λ), M(λ), P(λ), ∥β−βλ∥2 and T(λ) for Replicate 2 of the σ2 = 10-° case. The V(λ), (λ) and T(λ) curves tend to follow each other as predicted. plot of V(λ), T(λ), M(λ), P(λ), ∥β−βλ∥2 and T(λ) for Replicate 2 of the σ2 = 10-° case. The V(λ), (λ) and T(λ) curves tend to follow each other as predicted.

D. I. Gibbons [14] has recently completed a Monte Carlo comparison of 10 methods of choosing k. Three estimators, GCV, HKB (described in [23]), and RIDGM (described in [10,11]) were identified as the best performers in the examples studied. HKB and RIDGM use estimates of σ2. D. I. Gibbons [14] has recently completed a Monte Carlo comparison of 10 methods of choosing k. Three estimators, GCV, HKB (described in [23]), and RIDGM (described in [10,11]) were identified as the best performers in the examples studied. HKB and RIDGM use estimates of σ2.

## 6. CONCLUSIONS 6. CONCLUSIONS

The generalized cross-validation method for estimating the ridge parameter in ridge regression has been given. This estimate does not require an estimate of σ2, and thus may be used when the number of degrees of freedom for estimating σ2 is small or even; - l e , o  l  ? volves more than n parameters. The method may also be used to do subset selection or selection of principal components instead of ridge regression, or even to choose between various combinations of ridge, subset selection or principal components methods. A numerical example, briefly suggestive of the behavior of the method, has been carried out. It illustrates what an experimenter might wish to do to examine the properties of the method with respect to his/her design matrix. The generalized cross-validation method for estimating the ridge parameter in ridge regression has been given. This estimate does not require an estimate of σ2, and thus may be used when the number of degrees of freedom for estimating σ2 is small or even; -n l  l, o e l volves more than n parameters. The method may also be used to do subset selection or selection of principal components instead of ridge regression, or even to choose between various combinations of ridge, subset selection or principal components methods. A numerical example, briefly suggestive of the behavior of the method, has been carried out. It illustrates what an experimenter might wish to do to examine the properties of the method with respect to his/her design matrix.

## 7. ACKNOWLEDGMENTS 7. ACKNOWLEDGMENTS

The work of Gene H. Golub was initiated while a guest of the Eidgenössische Technische Hochschule. The work of Gene H. Golub was initiated while a guest of the Eidgenössische Technische Hochschule.

He is very pleased to acknowledge the gracious hospitality and stimulating environment provided by Professors Peter Henrici and Peter Huber. His research was supported in part under Energy Research and Development Administration Grant E(04-3) PA # 30, and in part under U.S. Army Grant DAHC04-75-G0185.

Michael Heath's research was supported in part under Energy Research and Development Administration Grant E(04-3) 326 PA #30.

The work of Grace Wahba was initiated while she was a visitor at the Oxford University Mathematical Institute at the invitation of Professor J. F. C. Kingman. The hospitality of Professor Kingman, the Mathematical Institute, and St. Cross College, Oxford, is gratefully acknowledged. Her research was supported by the Science Research Council (GB), and by U. S. Air Force Grant AF-AFOSR-2363-C.

####### REFERENCES

- [1] AKAIKE, H. (1974). A new look at the statistical model identification. IEEE Transaction on Automatic Control, AC19,6, 716–730.
- [2] ALLEN, D. M. (1971). Mean square error of prediction as a criterion for selecting variables. Technometrics, 13. 469–475.
- [3] ALLEN, D. M. (1974). The relationship between variable selection and data augmentation and a method for prediction. Technometrics, 16, 125–127.
- [4] ANDERSSEN, B. and BLOOMFIELD, P. (1974). Numerical differentiation procedures for non-exact data. Numer. Math., 22, 157–182.
- [5] ANDERSSEN, R. S. and BLOOMFIELD, P. (1974). A time series approach to numerical differentiation. Technometrics, 16, 69–75.
- [7] BELLMAN, R. (1960). Introduction to Matrix Analysis. New York: McGraw-Hill.
- [6] BAKER, C. T. H., FOX, L., MAYERS, D. F., and WRIGHT, K. (1964). Numerical solution of Fredholm integral equations of the first kind. Comp. J., 7, 141–148.
- [8] BERGER, J. (1976). Minimax estimation of a multivariate normal mean under arbitrary quadratric loss. J. Multivariate Analysis, 6, 256–264.
- [9] CRAVEN, P. and WAHBA, G. (1979). Smoothing noisy data with spline functions: estimating the correct degree of smoothing by the method of generalized cross-validation. Numer. Math., 31, 377–403.
- [10] DEMPSTER, A. P. (1973). Alternatives to least squares in multiple regression, In Multivariate Statistical Conference, Proceedings of the Research Seminar at Dalhousie University, Halifax, March 23-25, 1972, ed. by D. G. Kabe and R. P. Gupta.
- [11] DEMPSTER, A. P., SCHATZOFF, M., and WERMUTH, N. (1975). A simulation study of alternatives to ordinary least squares. J. Amer. Statist. Assoc., 70, 77–106.
- [12] FAREBROTHER, R. W. (1975). The minimum mean square error linear estimator and ridge regression. Technometrics, 17, 127–128.
- [13] GEISSER, S. (1975). The predictive sample reuse method with applications. J. Amer. Statist. Assoc., 70, 320–-328.
- [14] GIBBONS, D. 1. (1978). A simulation study of some ridge estimators. General Motors Research Laboratories, Research Publication GMR-2659, Warren, Michigan.
- [15] GOLDSTEIN, M., and SMITH, A. F. M. (1974). Ridge type estimators for regression analysis. J. Roy. Statist. Soc., Ser. B, 36, 284–291.


<!-- p:9 -->


- [16] GOLUB, G., and REINSCH, C. (1970). Singular value decomposition and least squares solutions. Numer. Math., 14, 403-420.
- [32] OBENCHAIN, R. L. (1975). Ridge Analysis following a preliminary test of the shrunken hypothesis. Technometrics, 17, 431–446.
- [17] GOLUB, G. H. (1973). Some modified matrix eigenvalue problems. SIAM Review, 15, 318–334.
- [18] GOLUB, G. H. and LUK, F. T. (1977). Singular value decomposition: applications and computations. Transactions of the Twenty-Second Conference of Army Mathematicians, 577– 605.
- [19] HANSON, R. J. (1971). A numerical method for solving Fredholm integral equations of the first kind using singular values. SIAM J. Num. Anal., 8, 616–622.
- [20] HEMMERLE, W. J. (1975). An explicit solution for generalized ridge regression. Technometrics, 17, 309–313.
- [21] HILGERS, J. W. (1976). On the equivalence of regularization and certain reproducing kernel Hilbert space approaches for solving first kind problems. SIAM J. Num. Anal., 13, 172– 184.
- [22] HOERL, A. E., and KENNARD, R. W. (1976). Ridge regression: iterative estimation of the biasing parameter. Comm. in Statist., A5, 77–88.
- [23] HOERL, A. E., KENNARD, R. W., and BALDWIN, K. F. (1975). Ridge regression: some simulations. Comm. in Statist., 4, 105–123.
- [24] HOUSEHOLDER, A. (1964). The Theory of Matrices in Numerical Analysis. New York: Blaisdell.
- [25] HUDSON, H. M. (1974). Empirical Bayes estimation. Technical Report No. 58, Stanford University, Department of Statistics, Stanford, CA.
- [26] LAWLESS, J. F. and WANG, P. (1976). A simulation study of ridge and other regression estimators. Comm. in Statist., A5, 307-324.
- [27] LINDLEY, D. V., and SMITH, A. F. M. (1972). Bayes estimate for the linear model (with discussion), part 1. J. Roy. Statist. Soc., B, 34, 1–41.
- [28] MALLOWS, C. L. (1973). Some comments on Cp. Technometrics, 15, 661–675.
- [29] MARQUARDT, D. W. (1970). Generalized inverses, ridge regression, biased linear estimation and nonlinear estimation. Technometrics, 12, 591–64.
- [30] MARQUARDT, D. W., and SNEE, R. D. (1975). Ridge regression in practice. The American Statistician, 29, 3-20.
- [31] MCDONALD, G. and GALARNEAU, D. (1975). A Monte Carlo evaluation of some ridge-type estimators. J. Amer. Statist. Assoc., 70, 407–416.
- [33] PARZEN, E. (1976). Time series theoretic nonparametric statistical methods. Preliminary Report, Statistical Science Division, SUNY, Buffalo, New York.
- [34] PARZEN, E. (1977). Forecasting and whitening filter estimation. Manuscript.
- [35] ROLPH, J. E. (1976). Choosing shrinkage estimators for regression problems. Comm. in Statist., A5, 789–802.
- [36] STONE, M. (1974). Cross-validatory choice and assessment of statistical prediction. J. Roy. Statist. Soc., B, 36, 111–147.
- [37] STONE, M. (1977). An asymptotic equivalence of choice of model by cross-validation and Akaike's criterion. J. Roy. Statist. Soc., B., 39, 44–47.
- [38] SWINDEL, B. F. (1976). Good ridge estimators based on prior information. Comm. in Statist., A5, 985–997.
- [39] THISTED, R. A. (1976). Ridge regression, minimax estimation, and empirical Bayes methods. Division of Biostatistics, Stanford University, Tech. Report No. 28.
- [40] VARAH, J. M. (1973). On the numerical solution of illconditioned linear systems with applications to ill posed problems. SIAM J. Num. Anal., 10, 257–267.
- [41] WAHBA, G. (1968). On the distribution of some statistics useful in the analysis of jointly stationary time series. Ann. Math. Statist., 39, 1849–1862.
- [42] WAHBA, G. (1976). A survey of some smoothing problems and the method of generalized cross-validation for solving them. In Proceedings of the Conference on the Applications of Statistics, held at Dayton, Ohio, June 14–17, 1976, ed. by P. R. Krishnaiah.
- [43] WAHBA, G. (1976). Optimal smoothing of density estimates. Classification and Clustering, pp. 423–458, ed. by J. Van Ryzin. New York: Academic Press.
- [44] WAHBA, G. (1977). The approximate solution of linear operator equations when the data are noisy. SIAM J. Num. Anal., 14, 651–667.
- [45] WAHBA, G., and WOLD, S. (1975). Periodic splines for spectral density estimation: the use of cross-validation for determining the correct degree of smoothing. Comm. in Statist., 4, 125–141.
- [46] WAHBA, G., and WOLD, S. (1975). A completely automatic French curve: fitting spline functions by cross-validation. Comm. in Statist., 4, 1–17.
