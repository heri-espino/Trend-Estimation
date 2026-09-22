---
id: "14_Smoothing_Noisy_Data_with_Spline_Functions"
source_pdf: "../pdf/14_Smoothing_Noisy_Data_with_Spline_Functions.pdf"
source_filename: "14_Smoothing_Noisy_Data_with_Spline_Functions.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
references_file: "../references/14_Smoothing_Noisy_Data_with_Spline_Functions.references.md"
---

<!-- p:1 -->

## Smoothing Noisy Data with Spline Functions

Estimating the Correct Degree of Smoothing by the Method of Generalized Cross-Validation*

Peter Craven1 and Grace Wahba2**

1 The Computer Laboratory, The University of Liverpool, Liverpool, England

2 Department of Statistics, University of Wisconsin, Madison, WI 53706, USA

Summary. Smoothing splines are well known to provide nice curves which smooth discrete, noisy data. We obtain a practical, effective method for estimating the optimum amount of smoothing from the data. Derivatives can be estimated from the data by differentiating the resulting (nearly) optimally smoothed spline.

with Eεi=0, Eεεj=σ2 δij. The error variance σ2 may be unknown. As an estimate of g we take the solution gn, λ to the problem: Find f∈ W(TM) to minimize 1 u 1 ∑ (f (t j) − yj)2 + λ ∫ ( f(m) (u))2 du. The function gn, λ is a smoothing polynomial n j=1 0 spline of degree 2m-1. Theparameter λ controls the tradeoff between the "roughness" of the solution, as measured by ∫ [f(m) (u)]2 du, and the infidelity to

We consider the model y = g(ti) + ε, i= 1, 2, .., n, t∈[0, 1], where g∈ W(m) = { f: f, f′,..., f(m− 1) abs. cont., f(m)∈ L2 [0, 1]}, and the {εi} are random errors

0

1 u the data as measured by 二 ∑ (f(tj)− yj)2, and so governs the average square nj=1 error R(λ; g)= R(λ) defined by

$$R ( \lambda ) = & \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g _ { n , \, \lambda } ( t _ { j } ) - g ( t _ { j } ) \right ) ^ { 2 } .$$

We provide an estimate λ, called the generalized cross-validation estimate, for the minimizer of R(λ). The estimate λ is the minimizer of V(λ) defined by V(λ)

$$\underset { n } { \text {Unclear} } \intertext { t h e c h s c r { I N I M } 2 C 1 $ o r $ K ( \lambda ) $ i n $ t r a c h s c r { I N O } $ o r $ V $ ( n ) $ o r $ A $ ( n ) $ e q $ ( n ) } & = \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, y \| ^ { 2 } / \left [ \frac { 1 } { n } T r a c ( I - A ( \lambda ) ) \right ] ^ { 2 } , \text { where } y = ( y _ { 1 } , \dots , y _ { n } ) ^ { t } \text { and } A ( \lambda ) \text { is the } n \\ & = \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, y \| ^ { 2 } / \left [ \frac { 1 } { n } T r a c ( I - A ( \lambda ) ) \right ] ^ { 2 } , \text { where } y = ( y _ { 1 } , \dots , y _ { n } ) ^ { t } \text { and } A ( \lambda ) \text { is the } n \\ & \quad n \\ & \quad \intertext { t h e c h s c r { I N I M } 2 C 2 $ o r $ K ( \lambda ) $ i n $ t r a c h s c r { I N O } $ o r $ V $ ( n ) $ o r $ A $ ( n ) }$$

× n matrix satisfying (gn(t1), ., gn, λ(t)) = A(λ) y. We prove that there exist a sequence of minimizers λ= λ(n) of EV (λ), such that as the (regular) mesh {ti}i= 1

¥ Research supported in part under U.S. Air Force Grant AF-AFOSR-77-3272 and by the Science Research Council (GB)

** To whom offprint requests should be sent


<!-- p:2 -->


9

becomes finer, lim ER(λ)/min ER(λ)↓1. A Monte Carlo experiment with n→8 λ several smooth g's was tried with m = 2, n = 50 and several values of σ2, and typical values of R(λ)/min R(λ) were found to be in the range 1.01–1.4. The λ derivative g' of g can be estimated by g', λ(t). In the Monte Carlo examples tried, 1 n the minimizer of R(λ)=− ∑ (g'n, λ(tj)-g′(tj)) tended to be close to the nj=1 minimizer of R(λ), so that Î was also a good value of the smoothing parameter for estimating the derivative. , '

Subject Classifications. MOS:65D10; CR: 5.17; MOS: 65D25.

### 1. Introduction

We consider the model

$$y ( t ) = g ( t ) + \varepsilon ( t ) , \quad t \in [ 0 , 1 ]$$

where g(t) is a "smooth" curve, and ε(t) is a white noise process, E ε(t) = 0, E ε(s) ε(t) = σ2, s=t, =0, otherwise (E is mathematical expectation). y(t) is observed for t=t1, t2, ..., tn, 0≤t1 &lt;t2 &lt; ... &lt;tn ≤1. It is desired to reconstruct g from the data y(t j) ≡ yj, j= 1,2, ..,n. We assume that g∈ Wim), where

$$W _ { 2 } ^ { ( m ) } = \{ g \colon ^ { ( \nu ) } \text {abs. cont., } \nu = 0 , 1 , \dots , m - 1 , \ g ^ { ( m ) } \in \mathcal { L } _ { 2 } \left [ 0 , 1 \right ] \} .$$

Our estimate of g is gn, , where gn, λ is the solution to the problem: Find f∈ W(m) to minimize

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( f ( t _ { j } ) - y _ { j } \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } d u .$$

The function gn, a is well known to be a polynomial smoothing spline of degree 2m — 1. See Reinsch [9, 10], Schoenberg [11], Wahba [13] for properties of smoothing splines. A Bayesian argument that the use of smoothing splines is appropriate when a certain prior distribution is attached to the {g(t)}= , may be obtained from the discussion in Kimeldorf and Wahba [7], see also [18].

The parameter λ, which must be chosen, controls the tradeoff between the "roughness" of the solution, as measured by

$$\begin{smallmatrix} 1 \\ \int [ f ^ { ( m ) } ( u ) ] ^ { 2 } \, d u \end{smallmatrix}$$

and the infidelity to the data as measured by

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( f ( t _ { j } ) - y _ { j } \right ) ^ { 2 } .$$

The problem is to obtain a good value of λ. Reinsch [9] suggests, roughly, that if σ2


<!-- p:3 -->


is known, then λ should be chosen so that the infidelity satisfies

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } ( g _ { n , \lambda } ( t _ { j } ) - y _ { j } ) ^ { 2 } = & \sigma ^ { 2 } .$$

Wahba [13] obtains theoretical results for the optimum choice of λ in the equally spaced data case when certain further smoothness and periodicity conditions are imposed. The optimum λ is defined as the λ which minimizes the true mean square error averaged over the data points. This true mean square error is defined as R(λ), given by

$$R ( \lambda ) = & \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g _ { n , \, \lambda } ( t _ { j } ) - g ( t _ { j } ) \right ) ^ { 2 } .$$

The results in [13] show that λ should be chosen so that the infidelity defined by the left-hand side of (1.4), is actually slightly less than σ2. However, this result is not practical, in that how much less depends on n as well as on the unknown g and on σ2, which may also be unknown.

If σ2 is known, then a good value of λ may be obtained from the data as follows: Define A(λ) as the n × n matrix depending on {ti}i=1 and λ satisfying

$$\begin{pmatrix} g _ { n , \, \lambda } ( t _ { 1 } ) \\ \vdots \\ g _ { n , \, \lambda } ( t _ { n } ) \end{pmatrix} = A ( \lambda ) \begin{pmatrix} y _ { 1 } \\ \vdots \\ y _ { n } \end{pmatrix} .$$

Since gn, λ(t) is a linear function of y1, y2, ..., y for each t, such A(λ) exists. Then

$$E R ( \lambda ) = E _ { n } ^ { \frac { 1 } { \| } } \| A ( \lambda ) \, y - g \| ^ { 2 }$$

where y=(y1, ..., yn)', g =(g(t1), ..., g(tn))', and "t" is transpose. The norm is the Euclidean norm. It follows from elementary calculations on (1.6) using the assumed mean and covariance properties of ε=(ε(t1), ..., ε(t)), that

$$E R ( \lambda ) = & \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, g \| ^ { 2 } + \frac { \sigma ^ { 2 } } { n } \text {Trace} \, A ^ { 2 } ( \lambda ) .$$

It is then trivial to demonstrate the following

Theorem 1.1. An unbiassed estimate of ER(λ) is given by Ř(λ) defined by

$$\hat { R } ( \lambda ) = & \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, y \| ^ { 2 } - \frac { \sigma ^ { 2 } } { n } \text {Tr} ( I - A ( \lambda ) ) ^ { 2 } + \frac { \sigma ^ { 2 } } { n } \text {Tr} \, A ^ { 2 } ( \lambda ) ,$$

that is

$$E \hat { R } ( \lambda ) = E R ( \lambda ) .$$

Therefore, the minimizer of Ř(λ) can be taken as a good choice of λ. An estimate of this type has been proposed by Mallows [8] in the context of ridge regression, see also Hudson [6].


<!-- p:4 -->


The main result of this paper is to obtain a good estimate of the minimizer of ER(λ) from the data which does not require knowledge of σ2. This estimate, to be called the generalized cross-validation (GCV) estimate, takes as the estimațe of λ, the minimizer of V(λ) defined by

$$V ( \lambda ) = & \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, y \| ^ { 2 } / \left [ \frac { 1 } { n } T r ( I - A ( \lambda ) ) \right ] ^ { 2 } .$$

We will demonstrate, under general conditions (to be given) on g, and on the mesh sequence {ti}i= 1 ≡ {tin}i= 1, n = 1, 2, ..., that, for large n, EV (λ) − σ2 ≈ ER(λ) ftor λ in the neighborhood of the minimizer of ER(λ).

As a consequence of this, we have the following:

Theorem 4.3. For g∈ W(m) and mild conditions on the mesh sequence {tn}= 1, there exists a sequence λ= λ(n) of minimizers of EV(λ) with the property that

$$\lim _ { \substack { n \to \infty \\ \lambda } } \frac { E R ( \tilde { \lambda } ) } { \min _ { \lambda } E R ( \lambda ) } = & 1 . \\ T I \colon _ { \substack { n = 0 \\ \lambda } }$$

This theorem says that the expected mean square error using λ tends to the minimum possible expected mean square error, as n→ ∞.

We now describe the origin of the GCV estimate. The intuitive idea of crossvalidation is quite simple and goes as follows: Let gn, be the smoothing spline using 8n, λ data point yk, as a measure of the goodnels of λ. Formally, let g,. be the function f∈ W() which minimizes

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( f ( t _ { j } ) - y _ { j } \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } d u ,$$

and let

$$V _ { o } ( \lambda ) = & \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left ( g _ { n , \lambda } ^ { [ k ] } ( t _ { k } ) - y _ { k } \right ) ^ { 2 } .$$

The (ordinary) cross-validation estimate of λ is defined to be the minimizer of V0(λ). The equally spaced data points case was considered in Wahba and Wold [15, 16], where the (ordinary) cross-validation estimate of λ was introduced. Fairly extensive Monte Carlo experiments [15] showed that the minimizer of V0(λ) was an amazingly good estimate of the minimizer of R(λ) over a variety of g and σ2 tried. Theoretical results related to the optimality of the minimizer of V0(λ) were also obtained for a special case equivalent to constraining g and g, ¿ to be periodic and requiring tj=j/n, j= 1, 2, ..., n. We shall call this the symmetric case.

Note that in the symmetric case all data points are treated symmetrically. That is, the prediction error at tk is weighted the same as at any other t j. In the general case, we let

$$V ( \lambda ) = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left ( g _ { n , \, \lambda } ^ { [ k ] } ( t _ { k } ) - y _ { k } \right ) ^ { 2 } w _ { k } ( \lambda ) ,$$


<!-- p:5 -->


where the weights wk(λ) are to compensate for nonequally spaced data points and the possible nonperiodicity of g. If

$$w _ { k } ( \lambda ) = \left [ ( 1 - a _ { k k } ( \lambda ) ) \left / \frac { 1 } { n } T r ( I - A ( \lambda ) ) \right ] ^ { 2 } ,$$

k = 1, 2, ..., n, where the {ak(λ)} are the diagonal elements of A(λ), then V(λ) of (1.13) becomes V(λ) of (1.9), and then (1.10) hols.

That is, we have obtained {wk} so that (1.10) holds. A different intuitive argument for the choice of V(λ) as in (1.9) is given in [17], and involves finding a rotation of Euclidean n-space which transforms the general problem into one equivalent to the symmetric problem and then doing ordinary cross validation. This point will be discussed further in Sect. 3.

In the process of proving (1.10) we have obtained a basis for the smoothing spline gr,  in terms of n periodic functions which are piecewise shifted Bernoulli polynomials with one knot, plus m + 1 polynomials of degree ≤m. (See Golomb [3] for earlier results on periodic splines.) An interesting fact about the n piecewise shifted Bernoulli polynomials is that, in the equally spaced data case their n × n Gram matrix is a circulant matrix. This representation will illuminate the remark that the smoothing spline for unequally spaced sampled non-periodic data is the natural generalization of the output of a low pass filter with the data as input.

In Sect. 2, we obtain the aforementioned representation of gn,λ in terms of polynomials plus periodic piecewise shifted Bernoulli polynomials, and we obtain the explicit formula for A(λ) that will be used in the proof of (1.10). In Sect. 3 we obtain a simplified form of V0(λ) of (1.11) and show that V(λ) of (1.13) with the weights {wk(λ)} given by (1.14) is equal to V(λ) of (1.9). In Sect. 4, we prove the main theorem, namely (1.10). In Sect. 5, we present some Monte Carlo examples illustrating the effectiveness of the method. Data according to the model (1.1) was generated with several smooth g's and range of values of σ2. Typical values of R(λ)/min R(λ) are to be found in the range 1.01–1.4 where Î is the minimizer of V(λ).

The minimizer of Ř(λ) of (1.8) and the value of λ satisfying (1.4) were also computed. The use of the minimizer of V(λ) was found to be roughly about as good as the minimizer of Ř(λ), while the use of (1.4) gave estimates of λ that were consistently too large.

We note that the method of generalized cross-validation is also applicable to choosing the regularization parameter in the method of regularization for solving Fredholm integral equations of the first kind, see [14].

### 2. Bernoulli Polynomials and Smoothing Splines

Let B,(t), r =0, 1, ... be the Bernoulli polynomials on t∈[0, 1]. The {B,} are defined 1 by letting B0(t)≡1, Br+1(t)=B,(t), and choosing the constant of in(r+1) dt tegration so that ∫ B,(u) d u =0, r = 1, 2, ... Letting [x] be the fractional part of x, 1

0


<!-- p:6 -->


we define

$$k _ { r } ( t ) = B _ { r } ( [ t ] ) / r ! .$$

Let Lk, k=0, 1, ... be the linear functionals

$$L _ { 0 } f & = \int _ { 0 } ^ { 1 } f ( u ) \, d u \\ L _ { k } f & = f ^ { ( k - 1 ) } ( 1 ) - f ^ { ( k - 1 ) } ( 0 ) \equiv \int _ { 0 } ^ { 1 } f ^ { ( k ) } ( u ) \, d u , \quad k = 1 , 2 , \dots \\$$

Then

$$L _ { k } ( k , ) & = 1 , \quad k = r \\ & = 0 , \quad k \neq r , \ k , r = 0 , 1 , 2 , \dots \ .$$

Define the "Bernoulli kernel" k,(s, t) by

$$k _ { r } ( s , t ) = - \sum _ { \nu = \frac { \infty } { v * 0 } } ^ { \infty } \frac { 1 } { ( 2 \pi i v ) ^ { \gamma } } e ^ { 2 \pi i v ( s - t ) } , \quad r = 1 , 2 , \dots$$

It is known (see Abramowitz and Stegun [1], p. 805), that

$$k _ { r } ( s , t ) = & \frac { 1 } { r ! } \, B _ { r } ( [ s - t ] ) = k _ { r } ( [ s - t ] ) ,$$

and it can be verified from the definition of k,(s, t) that

$$\frac { \partial ^ { p } } { \partial s ^ { p } } k _ { r } ( s , t ) = & k _ { r - p } ( s , t ) & p = & 1 , 2 , \dots , r - 2 \\ & \partial ^ { p }$$

$$and it can be verified from the definition of k , ( s , t ) \text { that} \\ \frac { \partial ^ { p } } { \partial s ^ { p } } k , ( s , t ) = & k _ { r - p } ( s , t ) \\ & p = 1 , 2 , \dots , r - 2 \\ \frac { \partial ^ { p } } { \partial t ^ { p } } k , ( s , t ) = & ( - ) ^ { p } k _ { r - p } ( s , t ) , \quad s , t \in [ 0 , 1 ] \\ \frac { \partial ^ { r - 1 } } { \partial s ^ { r - 1 } } k _ { r } , ( s , t ) = & k _ { 1 } ( s , t ) \\ & s , t \in [ 0 , 1 ] , \ s \neq t . \\ \frac { \partial ^ { r - 1 } } { \partial t ^ { r - 1 } } k _ { r } , ( s , t ) = & ( - 1 ) ^ { r - 1 } k _ { 1 } ( s , t ) \\ & 1 - \partial ^ { m } \\ \int _ { 0 } ^ { \frac { \partial ^ { m } } { 2 } } k _ { 2 m } ( s , u ) \frac { \partial ^ { m } } { \partial t ^ { m } } k _ { 2 m } ( t , u ) \, d u = ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( s , t ) . \\ \intertext { f u r e a n d w i s e d y o b t a i n a r e p r e s e n tation for g _ { n , \lambda } in t e r m s o f w i c e w i s } \text {Bernoulli polynomials}$$

We are now ready to obtain a representation for gn,  in terms of piecewise Bernoulli polynomials.

Theorem 2.1. The solution gn, λ, to the problem: Find f∈ W(TM) to minimize

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( f ( t _ { j } ) - y _ { j } \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } d u$$


<!-- p:7 -->


is, for n≥m, unique, and has the representation

$$g _ { n , \lambda } ( t ) = \sum _ { r = 0 } ^ { m } \theta _ { r } k _ { r } ( t ) + ( - 1 ) ^ { m - 1 } \sum _ { j = 1 } ^ { n } \alpha _ { j } k _ { 2 m } ( t , t _ { j } ) ,$$

where θ=(θ0, θ1, ...,θm) and α=(α1, α2, ...,α) are given by

$$\theta = & ( T ^ { t } M ^ { - 1 } T + \Delta ) ^ { - 1 } T ^ { t } M ^ { - 1 } y \\ \alpha = & M ^ { - 1 } ( y - T \theta ) \\ y = & ( y _ { 1 } , y _ { 2 } , \dots , y _ { n } ) ^ { t } ,$$

T is the n ×(m + 1) dimensional matrix with jrth entry

$$T _ { j , r } = & k _ { r } ( t _ { j } ) , \quad r = 0 , 1 , \dots , m \\ & j = 1 , 2 , \dots , n ,$$

Δ is the (m + 1) ×(m + 1) dimensional matrix of all zeroes except 1 in the (m + 1), (m + 1) position, M is given by

M=K+nλI

where K is the n ×n matrix with jkth entry Kjk,

$$K _ { j k } = ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( t _ { j } , t _ { k } )$$

and I is the n ×n identity matrix. The matrix A(λ) is given by

$$A ( \lambda ) = K M ^ { - 1 } \left [ I - T ( T ^ { \prime } M ^ { - 1 } T + \Delta ) ^ { - 1 } \, T ^ { t } \, M ^ { - 1 } \right ] + T ( T ^ { t } M ^ { - 1 } \, T + \Delta ) ^ { - 1 } \, T ^ { t } \, M ^ { - 1 } .$$

Proof. The expression for A(λ) follows immediately from (2.8). We first show that gn,λ∈span {{k,(·)}r=0{k2m(·, tj)}j=1}. This demonstration can be carried out a number of ways using known results on splines. We rely on the arguments in Kimeldorf and Wahba [7]. The reproducing kernel Q(s,t) for W(TM) endowed with the inner product

$$\langle f , g \rangle = \sum _ { r = 0 } ^ { m \wedge 1 } \left ( L _ { r } \, f \right ) ( L _ { r } \, g ) + \int _ { 0 } ^ { 1 } f ^ { ( m ) } \left ( u \right ) g ^ { ( m ) } ( u ) \, d u$$

is shown in Lemma 2.1, of the Appendix, to be

$$Q ( s , t ) = \sum _ { r = 0 } ^ { m } k _ { r } ( s ) \, k _ { r } ( t ) + ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( s , t ) .$$

It then follows from the arguments in [7] that gn, λ must lie in

$$\mathcal { S } = \text {span} \left \{ \{ k _ { r } ( \cdot ) \} _ { r = 0 } ^ { m - 1 } \cup \{ Q _ { t } , \} _ { j _ { r } = 1 } ^ { m } \right \} \text { where } Q _ { t _ { f } } ( \cdot ) \equiv Q ( \cdot , t _ { j } ) .$$

However S is contained in span {{k,(·)}r= 0 {k2m(·, tj)}j= 1} so that gn, λ has the representation (2.8a) for some θ, α. Substituting (2.8a) into (2.7), and using (2.6) gives


<!-- p:8 -->


384

$$\sum _ { j = 1 } ^ { n } ( g _ { n , \lambda } ( t _ { j } ) - y _ { j } ) ^ { 2 } + & n \lambda \int _ { 0 } ^ { 1 } \left ( g _ { n , 2 } ^ { ( m ) } ( u ) \right ) ^ { 2 } d u \\ & = \sum _ { j = 1 } ^ { n } \left [ \sum _ { \theta = 0 } ^ { m } \theta , k , ( t _ { j } ) + ( - 1 ) ^ { m - 1 } \sum _ { k = 1 } ^ { n } \alpha _ { k } k _ { 2 m } ( t _ { j } , t _ { k } ) - y _ { j } \right ] ^ { 2 } \\ & + n \lambda \left [ \sum _ { j = 1 } ^ { n } \sum _ { 1 \, k = 1 } ^ { n } \alpha _ { j } \alpha _ { k } ( - 1 ) ^ { m - 1 } k _ { 2 m } ( t _ { j } , t _ { k } ) + \theta _ { m } ^ { 2 } \right ] \\ & \equiv \| T \theta + K \alpha - y \| ^ { 2 } + n \lambda ( \alpha ^ { t } \, K \alpha + \theta _ { m } ^ { 2 } ) . \\ \intertext { The vectors } \intertext { The vectors } & \theta \, \text {and} \, \alpha \, \text {are to be chosen to minimize this expression. By differentiating}$$

The vectors θ and α are to be chosen to minimize this expression. By differentiating the right hand side of (2.11) with respect to θ and α and setting the result equal to 0 we obtain the Theorem.

We remark that (—)m− 1 k2m(t, tk), considered as a function of t is a monospline

so that g, λ is a polynomial spline of degree 2 m— 1, as is well known.

of degree 2m, that is, the sum of the monomial t2TM plus a polynomial spline of n degree 2m—1 (with a single knot at tk). However, it can be checked that ∑αj=0, j=1

When the knots {t j} are equally spaced, K, and hence M, are circulant matrices. The details are given in the (well-known)

$$L e m m a \, 2 . 2 \, \left \{ ( - 1 ) ^ { m - 1 } \, k _ { 2 m } \left ( \frac { j } { n } , \frac { k } { n } \right ) \right \} _ { j , k = 1 , \dots , n } = W D W ^ { * }$$

where "*" denotes complex conjugate transpose and W is the n × n unitary matrix with rsth entry Wrs given by

$$W _ { r s } = \frac { 1 } { \sqrt { n } } \, e ^ { 2 \pi i r s / n } ,$$

D is the diagonal matrix with vvth entry Dv given by

$$D \text { is the diagonal matrix with } v \text { with } D _ { v v } \text { given by} \\ D _ { v v } = \lambda _ { n } ^ { 2 m } \\ \text {where} \\ \lambda _ { n } ^ { r } = n \sum _ { \xi = - \infty } ^ { \infty } \frac { 1 } { [ 2 \pi ( v + \xi n ) ] ^ { r } } \quad ( \lambda _ { v n } ^ { r } \equiv \lambda _ { n - v , n } ^ { r } ) \\ \lambda _ { n n } ^ { r } = n \sum _ { \xi \neq 0 } ^ { \infty } \frac { 1 } { [ 2 \pi \xi n ] ^ { r } } . \\ \text {Proof.}$$

Proof.

$$P r o f . & & P r o f . & & ( - 1 ) ^ { m - 1 } \, k _ { 2 m } \left ( \frac { j } { n } , \frac { k } { n } \right ) = \sum _ { \substack { v _ { v } = - \infty \\ v \neq 0 } } ^ { \infty } \frac { 1 } { ( 2 \pi v ) ^ { 2 } m } \, e ^ { 2 \pi i v ( j - k ) / n } \\ & & = \sum _ { \substack { v = 1 \\ ( v , \xi ) \neq ( n , - 1 ) } } ^ { n } \frac { \infty } { \sum _ { \substack { v = 1 \\ ( v , \xi ) \neq ( n , - 1 ) } } ^ { 1 } } \frac { 1 } { e ^ { 2 \pi i v ( j - k + \xi n ) / n } } \\ & & = \sum _ { \substack { v = 1 \\ ( v , \xi ) \neq ( n , - 1 ) } } ^ { n } \frac { \infty } { \sum _ { \substack { v = 1 \\ ( v , \xi ) \neq ( n , - 1 ) } } ^ { 1 } } \frac { 1 } { e ^ { 2 \pi i v ( j - k ) / n } } \\$$


<!-- p:9 -->


The λ'' can be expressed in terms of the polygamma function, see Abramowitz and Stegun [1], Sect. 6.4. However, sufficient computational accuracy will usually be obtained with only a few terms in (2.12).

### 3. The Generalized Cross-Validation Function V(λ)

We first obtain a simplified representation for the (ordinary) cross-validation function V0(λ) defined by

$$V _ { 0 } ( \lambda ) = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left ( g _ { 1 } ^ { 1 } \right )$$

Recall that ,[k] is the solution to the problem: Find f∈ W(m) to minimize

$$\frac { 1 } { n } \sum _ { \substack { j = 1 \\ j + k } } ^ { n } ( f ( t _ { j } ) - y _ { j } ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } ( f ^ { ( m ) } ( u ) ) ^ { 2 } \, d u .$$

original (n-data point) minimization problem (1.2) with the data y1, y2, .., yk– 1, gn,λ(t), k+ 1 ., y, we get g g[k] g[k] for the solution. This is the content of 8n, λ

Lemma 3.1. Let n≥m and let gn, λ(t; k, zk) be the solution to the problem: Find f∈ Wm) to minimize

$$\frac { 1 } { n } \left [ ( f ( t _ { k } ) - z _ { k } ) ^ { 2 } + \sum _ { \substack { j = 1 \\ j \neq k } } ^ { n } ( f ( t _ { j } ) - y _ { j } ) ^ { 2 } \right ] + \lambda \int _ { 0 } ^ { 1 } ( f ^ { ( m ) } ( u ) ) ^ { 2 } \, d u .$$

Then

$$g _ { n , \lambda } ( t ; k , g _ { n , \lambda } ^ { [ k ] } ( t _ { k } ) ) = g _ { n , \lambda } ^ { [ k ] } ( t ) .$$

Proof. Let h=8 [k] [k] (tk) and let f be any element of W(TM) different from h. gn, λ Then let

$$1$$

$$\text {Then} \\ \frac { 1 } { n } \left [ \sum _ { j \neq k } ^ { n } ( h ( t _ { j } ) - y _ { j } ) ^ { 2 } + ( h ( t _ { k } ) - z _ { k } ) ^ { 2 } \right ] + \lambda \int _ { 0 } ^ { 1 } ( h ^ { ( m ) } ( u ) ) ^ { 2 } \, d u \\ = - \left [ \sum _ { j \neq k } ^ { 1 } ( h ( t _ { j } ) - y _ { j } ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } ( h ^ { ( m ) } ( u ) ) ^ { 2 } \, d u \right ] \\ \quad \ \ 1 \\ \quad \ < - \left [ \sum _ { j \neq k } ^ { n } ( f ( t _ { j } ) - y _ { j } ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } ( f ^ { ( m ) } ( u ) ) ^ { 2 } \, d u \right ] \\ \leq \frac { 1 } { n } \left [ \sum _ { j \neq k } ^ { n } ( f ( t _ { j } ) - y _ { j } ) ^ { 2 } + ( f ( t _ { k } ) - z _ { k } ) ^ { 2 } \right ] + \lambda \int _ { 0 } ^ { 1 } ( f ^ { ( m ) } ( u ) ) ^ { 2 } \, d u .$$


<!-- p:10 -->


Comparing the left and rightmost expressions, we see that h solves the n-data point minimization problem with yk replaced by zk.

The results of Lemma 3.1 allow us to prove

#### Lemma 3.2.

$$g _ { n , \, \lambda } ^ { [ k ] } \left ( t _ { k } \right ) - y _ { k } = & \left ( g _ { n , \, \lambda } ( t _ { k } ) - y _ { k } \right ) / \left ( 1 - \frac { \partial } { \partial y _ { k } } \, g _ { n , \, \lambda } ( t _ { k } ) \right ) .$$

Proof. Let zk = g,λ (t). Then Lemma 3.1 and the fact that for each t, gn, (t) depends [k] linearly on yk, gives

$$\text {linearly on } y _ { k } , \text { gives} \\ z _ { k } = g _ { n , \lambda } ( t ; k , z _ { k } ) = g _ { n , \lambda } ( t _ { k } ; k , y _ { k } ) + ( z _ { k } - y _ { k } ) \frac { \partial g _ { n , \lambda } ( t _ { k } ) } { \partial y _ { k } } . \\ = & g _ { n , \lambda } ( t _ { k } ) + ( z _ { k } - y _ { k } ) \frac { \partial g _ { n , \lambda } ( t _ { k } ) } { \partial y _ { k } } \\$$

and the result follows after some algebraic manipulation.

Denoting the entries of A(λ) by ajk, we have

$$g _ { n , \lambda } ( t _ { k } ) \dot { = } \sum _ { j = 1 } ^ { n } a _ { k j } y _ { j }$$

and so

$$\frac { \partial g _ { n , \lambda } ( t _ { k } ) } { \partial y _ { k } } = a _ { k k }$$

and it follows from Lemma 3.2 that

$$V _ { 0 } ( \lambda ) = \frac { 1 } { n } \sum _ { k = 1 } ^ { n } \left \{ \left ( \sum _ { j = 1 } ^ { \prime } a _ { k , j } y _ { j } - y _ { k } \right ) ^ { 2 } / ( 1 - a _ { k } ) ^ { 2 } \right \} .$$

To motivate the definition of V(λ) consider the periodic version of the smoothing problem: it is: Find g∈ W(m), periodic and with integral 0, to minimize

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( f ( t _ { j } ) - y _ { j } \right ) ^ { 2 } + \lambda \, \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } \, d u .$$

The function g periodic with integral 0 in this context means

$$L _ { k } g = 0 , \quad k = 0 , 1 , \dots , m .$$

It can be shown that the solution hn, λ is given by

$$n$$

$$h _ { n , \lambda } ( t ) & = \sum _ { j = 1 } ^ { n } \, \alpha _ { j } ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( t , t _ { j } ) \\ \text {where} & \\ & \alpha = ( K + n \lambda I ) ^ { - 1 } \, y \equiv M ^ { - 1 } \, y .$$


<!-- p:11 -->


Here the role of A is played by KM−1. If tj=j/n, j=1, 2, .., n, then KM−1 is 1 n circulant for every λ and hence constant down the diagonals, akk 三 nj=1 一 ∑ ajj

$$\equiv \frac { 1 } { n } \text {Trace} \, A \text { and } V _ { 0 } ( \lambda ) \text { becomes}$$

1

$$n & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & & &$$

(This expression is given in Wahba and Wold [16] for the periodic, equally spaced case considered there.)

To obtain generalized cross-validation from "ordinary" cross-validation in general, one rotates the coordinate system so the matrix, call it Ä(λ), which plays the role in the new coordinate system of the prediction matrix A(λ), is circulant. Since A is symmetric this can always be done by writing A(λ)= UD2(λ) Ut where D2 is diagonal and U is orthogonal. Then, letting Γ = WUt, Ā(λ) = ΓA(λ) Γ is circulant. Let y = Γ y. Then the " smoothed" y is (gn, λ(t1) . .., gn, (t,)t = Γ A(λ) y = Å(λ) y, say. oo     ,   oa- io o n

We remark that inspection of h,  [Eq. (3.2)] reveals the "low pass filter" character of the smoothing spline in the periodic, equally spaced data case. From Lemma 2.2 and Eq. (3.2) we find that the sample Fourier coefficients {hn, λ, v} of hn, a,

$$h _ { n , \lambda , \nu } \dot { \underline { = } } _ { n } ^ { 1 } \sum _ { j = 1 } ^ { n } h _ { n , \lambda } \left ( \frac { j } { n } \right ) e ^ { - 2 \pi i \nu j / n }$$

are related to the Fourier coefficients {h} of the data

$$\hat { h } _ { \nu } \dot { = } \frac { 1 } { n } \sum _ { j = 1 } ^ { n } y \left ( \frac { j } { n } \right ) e ^ { - 2 \pi i v j / n }$$

by the equations

$$h _ { n , \, \lambda , \, \nu } = f _ { \nu } \hat { h } _ { \nu } , \quad v = 1 , 2 , \dots , n ,$$

where

$$f _ { v } = & \frac { 1 } { 1 + n \lambda / \lambda _ { v n } ^ { 2 m } } . \\$$

When v «n we may approximate the summation for λ in (2.12) by the ξ=0 term and so obtain

$$f _ { \nu } \approx & \frac { 1 } { 1 + n \, \lambda ( 2 \pi \, v ) ^ { 2 m } } = B \left ( \frac { v } { v _ { 0 } } \right ) B ^ { * } \left ( \frac { \nu } { v _ { 0 } } \right )$$

where B ν is the Butterworth filter, well known to electrical engineers, having vo 1 half power point v0 = 2π(nλ)1/2m


<!-- p:12 -->


### 4. Optimal Properties of the Generalized Cross-Validation Estimate of λ

Recall that the true mean square error is given by

$$R ( \lambda ) = & \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left ( g _ { n , \lambda } ( t _ { i } ) - g ( t _ { i } ) \right ) ^ { 2 } \\ = & \frac { 1 } { n } \left \| A ( \lambda ) \, y - g \right \| ^ { 2 }$$

and the cross-validation function V(λ) is given by

$$V ( \lambda ) = \frac { \lim _ { \substack { n \\ \left ( 1 - - T r A ( \lambda ) \right ) Y \right | ^ { 2 } } } ^ { 1 } } { \left ( 1 - - T r A ( \lambda ) \right ) ^ { 2 } } .$$

The general idea is that one wishes to choose λ to minimize R(λ). This cannot be done directly, of course, since R(λ) involves the unknown g. If σ2 is known, then the minimizer of Ř (λ) of (1.8) can be used to estimate the λ which minimizes R(λ). If σ2 is not known, we will show that the minimizer of V(λ) can be used.

To demonstrate the usefulness of V(λ), we must distinguish two cases. If g(·)∈πm- 1, where πm-1 are the polynomials of degree m-1 or less, we shall first show that ER(λ) and EV(λ) are both minimized for λ = ∞. (Recall that fn,  is the m-1st degree polynomial best fitting the data in the least squares sense.) In general, we will show that if λ is the minimizer of EV(λ), then the inefficiency I* of the method of generalized cross validation, defined by

$$I ^ { * } = \frac { E R ( \tilde { \lambda } ) } { \min _ { \tilde { \lambda } } E R ( \tilde { \lambda } ) }$$

tends to 1 as n→ ∞. Thus, the mean square error when λ is estimated by minimizing V should be close to the minimum possible mean square error.

It follows immediately that I* = 1 if g∈πm- 1, since ER(·) and EV(·) have the same minimizer. In the general case g∈ W(TM), gπm– 1, it will turn out that λ and λ*, the minimizers of EV(λ) and ER(λ) respectively, must satisfy λ→0, λ*→0, 1n     d  dd        d. First we show that

$$\left | \frac { E R ( \lambda ) + \sigma ^ { 2 } - E V ( \lambda ) } { E R ( \lambda ) } \right | \leq & h ( \lambda )$$

where h(λ) is a small quantity to be defined. We will then show that

$$I ^ { * } \equiv \frac { R ( \tilde { \lambda } ) } { R ( \lambda ^ { * } ) } \leqq \frac { 1 + h ( \lambda ^ { * } ) } { 1 - h ( \tilde { \lambda } ) } .$$

Finally we show that h(λ) = O(1/n λ1/2m) and that λ*, λ must satisfy 1/n(λ*)1/2m → 0,


<!-- p:13 -->


1/n(λ)1/2m → 0, from which it will follow that (1 + h(λ*))/(1 − h(λ)) ↓ 1 and hence I* ↓ 1. Let

$$L \text { } & \quad \text {Let} \\ b ^ { 2 } ( \lambda ) = & \frac { 1 } { n } g ^ { t } ( I - A ( \lambda ) ) ^ { 2 } \, g = & \frac { 1 } { n } \left \| ( I - A ( \lambda ) ) \, g \right \| ^ { 2 } \\ \mu _ { 1 } ( \lambda ) = & \frac { 1 } { n } T r \, A ( \lambda ) \\ \mu _ { 2 } ( \lambda ) = & \frac { 1 } { n } T r \, A ^ { 2 } ( \lambda ) .$$

Then

$$E R ( \lambda ) = & b ^ { 2 } ( \lambda ) + \sigma ^ { 2 } \, \mu _ { 2 } ( \lambda ) \\ E V ( \lambda ) = & \frac { b ^ { 2 } ( \lambda ) + \sigma ^ { 2 } ( 1 - 2 \mu _ { 1 } ( \lambda ) + \mu _ { 2 } ( \lambda ) ) } { [ 1 - \mu _ { 1 } ( \lambda ) ] ^ { 2 } } .$$

We first consider the case g(·)∈πm− 1. In this case g = (g(t1), g(t2), ..., g(t)) is a linear combination of the first m columns of T and so (I — A(λ)) g = 0 for all λ and b(λ)≡0. Thus the minimization of ER(λ) reduces to the minimization of Tr A2(λ), which is clearly minimized for λ= ∞. Similarly EV(λ) becomes

$$E V ( \lambda ) = ( 1 - 2 \, \mu _ { 1 } ( \lambda ) + \mu _ { 2 } ( \lambda ) ) / ( 1 - \mu _ { 1 } ( \lambda ) ) ^ { 2 } .$$

Now I – A(λ) has m zero eigenvalues, and the remaining n –m eigenvalues can be shown to be of the form nλ(nλ+ξv)-1, y=1,2,..,n-m where ξ1m details), and so the above expression for EV(λ) becomes

$$d e t a l s ) , \, a n d \, s o \, t h e \, a b o v e \, e x p r e s s l i o n \, f o r \, E V ( \lambda ) \, \text { becomes} \\ E V ( \lambda ) = \frac { 1 } { n } \sum _ { v = 1 } ^ { n - m } \left ( \frac { n \, \lambda } { n \, \lambda + \xi _ { v n } } \right ) ^ { 2 } \Big / \left ( \frac { 1 } { n } \sum _ { v = 1 } ^ { n - m } \frac { n \, \lambda } { n \, \lambda + \xi _ { v n } } \right ) ^ { 2 } \\ \frac { 1 } { n } \sum _ { v = 1 } ^ { n - m } \left ( \frac { n \, \lambda } { n - m } \sum _ { v = 1 } ^ { 2 } \left ( \frac { n \, \lambda } { n \, \lambda + \xi _ { v n } } \right ) ^ { 2 } \right ) \\ = \frac { 1 } { \left ( \frac { n - m } { n } \right ) } \frac { 1 } { \left [ \frac { 1 } { n - m } \sum _ { v = 1 } ^ { n - m } \left ( \frac { n \, \lambda } { n \, \lambda + \xi _ { v n } } \right ) \right ] ^ { 2 } } \geq \frac { 1 } { \left ( \frac { n - m } { n } \right ) } , \\ \intertext { a n d \, the \, minimum \, is \, a t t a i n e d \, if \, a n d \, \text { only if } \lambda = \infty . }$$

and the minimum is attained if and only if λ = ∞. We now proceed to the general case. We have

Theorem 4.1.

$$\frac { E R ( \lambda ) + \sigma ^ { 2 } - E V ( \lambda ) } { E R ( \lambda ) } = \frac { - \mu _ { 1 } ( 2 - \mu _ { 1 } ) } { ( 1 - \mu _ { 1 } ) ^ { 2 } } + \frac { \sigma ^ { 2 } } { b ^ { 2 } + \sigma ^ { 2 } \, \mu _ { 2 } } \cdot \frac { \mu _ { 1 } ^ { 2 } } { ( 1 - \mu _ { 1 } ) ^ { 2 } } \\$$

and so

$$\underline { | E R ( \lambda ) + \sigma ^ { 2 } - E V ( \lambda ) | } _ { < h ( \lambda ) }$$


<!-- p:14 -->


where

$$h ( \lambda ) = \left [ 2 \, \mu _ { 1 } ( \lambda ) + \frac { \mu _ { 1 } ^ { 2 } ( \lambda ) } { \mu _ { 2 } ( \lambda ) } \right ] \, \frac { 1 } { ( 1 - \mu _ { 1 } \, ( \lambda ) ) ^ { 2 } } \, .$$

Proof of Theorem. The result follows trivially from

$$E R \left ( \lambda \right ) + \sigma ^ { 2 } - E V ( \lambda ) = E R ( \lambda ) \left ( 1 - \frac { 1 } { ( 1 - \mu _ { 1 } ( \lambda ) ) ^ { 2 } } \right ) + \sigma ^ { 2 } \frac { \mu _ { 1 } ^ { 2 } ( \lambda ) } { ( 1 - \mu _ { 1 } ( \lambda ) ) ^ { 2 } } .$$

From Theorem 4.1 one can deduce

Theorem 4.2. Let λ* be the minimizer of ER (λ). Then EV (λ) has a minimum λ so that the "expectation inefficiency" I* defined by

$$I ^ { * } = \frac { E R ( \tilde { \lambda } ) } { E R ( \lambda ^ { * } ) }$$

satisfies

$$I ^ { * } \leq & \frac { 1 + h ( \lambda ^ { * } ) } { 1 - h ( \hat { \lambda } ) } .$$

Proof. Let Λ={λ: 0≤λ≤∞, EV(λ)−σ2≤R(λ*)(1 + h(λ*))}.

Since

$$E R ( \lambda ) ( 1 - h ( \lambda ) ) < E V ( \lambda ) - \sigma ^ { 2 } < E R ( \lambda ) ( 1 + h ( \lambda ) ) , \quad 0 \leq \lambda < \infty \, ,$$

and ER, EV, and h are continuous functions of λ, then A is a non-empty closed set. If 0 is not a boundary point of A, then EV(λ) has a minimum in the interior of A, (or possibly at ∞) call it λ (see Fig. 1). Now by Theorem 4.1

$$E R ( \tilde { \lambda } ) ( 1 - h ( \tilde { \lambda } ) ) < E V ( \tilde { \lambda } ) - \sigma ^ { 2 } < E R ( \lambda ^ { * } ) ( 1 + h ( \lambda ^ { * } ) )$$

If A includes 0, then λ may be on the boundary of A, i.e., λ =0, but the above bound on I* still holds. Our aim now is to prove that h(λ*) and h(λ) →0 as n → ∞. We will use several lemmas, whose proofs we relegate to the Appendix.

~jr Lemma 4.1. If g∈ W(m),

Fig. 1. Graphical suggestion of the proof of Theorem 4.2

<!-- p:15 -->


$$b ^ { 2 } ( \lambda ) \leqq \lambda \int _ { 0 } ^ { 1 } \left ( g ^ { ( m ) } ( u ) \right ) ^ { 2 } d u$$

Lemma 4.2. Let {ti}i= 1 ≡ {tin}i= 1 satisfy

$$\int _ { 0 } ^ { \imath _ { n } } w ( u ) \, d u = i / n , \quad i = 1 , 2 , 3 , \dots , n , \ n = 1 , 2 , \dots$$

where w(u) is a continuous strictly positive weight function. Then if g∉πm\_ 1, (and not identically 0) and λ is bounded away from 0 as n→ ∞, then b2(λ) is also bounded away from 0.

Lemma4.3. Let {tin}i=1 satisfy the hypothesis of Lemma 4.2 with 0&lt;α≤w(t) ≤β&lt;∞.Then

$$\leq & \beta < \infty . \text { Then } \\ & \frac { k _ { m } } { \beta ^ { 1 / 2 m } } + o ( 1 ) \leq n \lambda ^ { 1 / 2 m } \mu _ { 1 } ( \lambda ) \leq & \frac { k _ { m } } { \alpha ^ { 1 / 2 m } } + o ( 1 ) \\ & \frac { l _ { m } } { \beta ^ { 1 / 2 m } } + o ( 1 ) \leq & n \lambda ^ { 1 / 2 m } \mu _ { 2 } ( \lambda ) \leq & \frac { l _ { m } } { \alpha ^ { 1 / 2 m } } + o ( 1 ) , \\ \intertext { w h e r e } o ( 1 ) = & O ( \lambda ) + O ( 1 / n \lambda ^ { 1 / 2 m } ) , \quad \text {as } \lambda \to 0 , \ n \lambda ^ { 1 / 2 m } \to \infty \\ \text {and} \\ & k _ { m } = \int \frac { \infty } { \Gamma } \int \frac { d x } { \Gamma } , \quad l _ { m } = \int \left ( \frac { \infty } { \Gamma } \frac { d x } { \Gamma } \right ) ,$$

$$k _ { m } = \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + x ^ { 2 m } ) } , \quad l _ { m } = \int _ { 0 } ^ { \infty } \frac { d x } { ( 1 + x ^ { 2 m } ) ^ { 2 } } .$$

Conversely, if n λ1/2m is bounded away from 0, then so are μ1(λ) and μ2(λ). We remark that it is a consequence of Lemma 4.3 that μ2(λ)/μ2(λ) →0. We conclude from Lemmas 4.1-4.3 that if g(·)∉πm−1, then, as λ→0, n λ1/2m→∞,

$$E R ( \lambda ) = b ^ { 2 } ( \lambda ) + \sigma ^ { 2 } \, \mu _ { 2 } ( \lambda ) = O ( \lambda ) + O ( 1 / n \, \lambda ^ { 1 / 2 \, m } ) \to 0 ,$$

and if either λ or 1/n λ1/2m is bounded away from 0, ER(λ) does not tend to 0. Thus, to minimize ER(λ), we must have λ* →0, n(λ*)1/2m→ ∞, so that h(λ*)→0. Now it can be checked that EV(λ)≥σ2. Furthermore EV(λ)↓σ2 since EV(λ)-σ2 ≤ER(λ*)(1 +h(λ*))→0. If g∉πm−1, it is necessary that λ→0, n(λ)1/2m→∞ in order that EV(λ) ↓σ2, and so it can be concluded that h(λ) →0 as n→ ∞.

Combining the above arguments with Theorem 4.2 gives the following main

i tin Theorem 4.3. Let g(·)∈W{m), and let {tin}i=1 satisfy 一 w(u) du, where w(u) is a n 0 strictly positive continuous weight function. Then there exist a sequence λ = λ(n) of minima of EV(λ) such that

$$\lim _ { n \to \infty } \frac { E R ( \tilde { \lambda } ) } { E R ( \lambda ^ { * } ) } = 1 .$$


<!-- p:16 -->


### 5. Numerical Results

We have tried the method on artificial data of the form y(ti) = g(ti) + ε, where ε are normally distributed pseudo-random numbers with mean 0 and variance σ2, and m =2. For m = 2, g, λ is a cubic smoothing spline.

In the m =2 case, it can be established from Reinsch [9], p. 179, that

$$I - A ( \lambda ) = \tilde { Q } ( \tilde { Q } ^ { t } \tilde { Q } + p \, \tilde { T } ) ^ { - 1 } \, \tilde { Q } ^ { t }$$

where

$$p = 1 / n \dot { \lambda } ,$$

Q is the n ×(n−2) dimensional tridiagonal matrix with entries ij, i= 1, 2, ..., n, j= 1, 2, ..., n − 2, given by

$$\tilde { q } _ { i , i + 1 } = & i / h _ { i + 1 } , \quad \tilde { q } _ { i i } = - 1 / h _ { i } - 1 / h _ { i + 1 } , \quad \tilde { q } _ { i + 1 , i } = 1 / h _ { i + 1 } ,$$

where hi = ti + 1 − ti, and Ī is the (n − 2) × (n − 2) dimensional tridiagonal matrix with entries tij, i, j = 1, 2, ..., n − 2 given by

$$\tilde { t } _ { i i } = 2 ( h _ { i } + h _ { i + 1 } ) / 3 , \quad \tilde { t } _ { i , i + 1 } = \tilde { t } _ { i + 1 , i } = h _ { i + 1 } / 3 .$$

The matrix  is strictly positive definite (assuming h&gt; 0). Let F = Qĩ − 1/2, where 1 − 1/2 is the symmetric square root of T− 1. When hi ≡−, i ,i=1, 2, ..., n, τ − 1/2 can n

be found analytically from the formula

$$\begin{pmatrix} \beta & \beta & 0 \\ \beta & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \cdot \\ \cdot & \cdot & \beta \\ \beta & \alpha \end{pmatrix} = \dot { R } D r ^ { \prime }$$

where

$$\Gamma _ { j k } = \sqrt { \frac { 2 } { n + 1 } } \sin \frac { j k \pi } { n + 1 }$$

jπ and D is the diagonal matrix with jjth entry α+2βcos thus n+1'

$$\tilde { T } ^ { - 1 / 2 } = \Gamma D ^ { - 1 / 2 } \, \Gamma ^ { t } .$$

Then

$$I - A = F ( F ^ { t } F + p I ) ^ { - 1 } \, F ^ { t } .$$


<!-- p:17 -->


Let the singular value decomposition of F be (see [5])

$$F = U D V ^ { T }$$

where U and V are n × (n−2) and (n-2) × (n-2) orthogonal matrices and D has the (non-zero) singular values of F, call them d1, d2, ., d\_2 on the diagonal and zeroes elsewhere. Then

$$I - A = U \begin{pmatrix} \frac { d _ { 1 } ^ { 2 } } { d _ { 1 } ^ { 2 } + p } & 0 \\ & \ddots \\ 0 & \cdot \frac { d _ { n - 2 } ^ { 2 } } { d _ { n - 2 } ^ { 2 } + p } \end{pmatrix} U ^ { t }$$

and

$$V ( p ) = & - \sum _ { n } ^ { 1 - n - 2 } \left ( \frac { d _ { j } ^ { 2 } } { d _ { j } ^ { 2 } + p } \right ) ^ { 2 } z _ { j } ^ { 2 } / \left [ \frac { 1 } { n } \sum _ { j = 1 } ^ { n - 2 } \left ( \frac { d _ { j } ^ { 2 } } { d _ { j } ^ { 2 } + p } \right ) \right ] ^ { 2 } \\$$

where

$$z = ( z _ { 1 } , \dots , z _ { n - 2 } ) ^ { t } = U ^ { t } \, y$$

The numerical experiments were conducted as follows: To conform to Reinsch's formulae, λ is everywhere replaced by p = 1/n λ. For given g, σ2, and n, data y, i= 1, 2, ..., n, were generated by

$$y _ { i } = g \left ( \frac { i - 1 } { n } \right ) + \varepsilon _ { i } , \quad i = 1 , 2 , \dots , n ,$$

where the ε are pseudo-random variates with mean 0 and variance σ2. V(p) is computed using (5.5), for log1o p in increments of 1/9, and the minimizing p, call it p, was obtained by global search. Then gn, λ for λ= 1/np is computed using Reinsch [9], (Eqs. 8, 9, 13 and 14), and R(p),

$$R ( p ) = & \frac { 1 } { n } \sum _ { i = 1 } ^ { n } \left ( g ( t _ { i } ) - g _ { n , \, \lambda } ( t _ { i } ) \right ) ^ { 2 }$$

is obtained for comparison.

Test functions of the form

$$g ( t ) = \sum _ { j = 1 } ^ { r } w _ { j } \beta _ { p _ { j } , q _ { j } } ( t ) ,$$

where

$$\beta _ { p q } ( t ) = & \frac { \Gamma ( p + q ) } { \Gamma ( p ) \, \Gamma ( q ) } \, t ^ { p - 1 } \, ( 1 - t ) ^ { q - 1 }$$

and Γ is the gamma function were used.


<!-- p:18 -->


Fig. 2. Examples I, II, and III, g, gn, λ, and the data

The examples are

| Example I   | r = 3   | wl =0.2   | pa = 4   | q1=15   |
|-------------|---------|-----------|----------|---------|
|             |         | w2=0.7    | p2 = 5   | q2 = 7  |
|             |         | w3 =0.1   | p3=12    | q3= 5   |
| Example II  | r = 2   | wl =0.4   | pt=12    | ql= 7   |
|             |         | w/=0.6    | p2 = 4   | q2=ll   |
| Example III | r=3     | w 1 =0.5  | pl=10    | q1=30   |
|             |         | w 2 =0.2  | P2 =20   | q2 =20  |
|             |         | w3 =0.3   | P3=30    | q3=10   |

i Figure2 gives plots of the original function g(t), the data y=g + εi, n i = 1, 2, ..., n, and gn, (t), λ = 1/n p, and p is the minimizer of V (p). Here σ = 0.1 and the number of data points n = 50. Figure 3 gives plots of V(p), Ř(p), and R(p).

Ř(p) is defined by (1.8) and is computed by

$$\hat { R } ( p ) = & \frac { 1 } { n } \sum _ { j = 1 } ^ { n - 2 } \left ( \frac { d _ { j } ^ { 2 } } { d _ { j } ^ { 2 } + p } \right ) ^ { 2 } z _ { j } ^ { 2 } + \frac { 2 \sigma ^ { 2 } } { n } \sum _ { j = 1 } ^ { n - 2 } \left ( \frac { d _ { j } ^ { 2 } } { d _ { j } ^ { 2 } + p } \right ) - \sigma ^ { 2 } .$$

The minima of each of these curves is marked with a circle. Reinsch's suggestion for choosing p [Eq. (1.4)] when σ2 is known, was also implemented. In our notation, his suggestion becomes: Choose p so that S(p)/σ2=1. To evaluate this suggestion, S(p) is also plotted, and the point S(p)=σ2 is also marked with a circle.

In each example I, II, III it is seen that R(p) tracks R(p), and in the neighborhood of the minimum of R(p), V(p)≈R(p) + constant, where the constant is around σ2. (Note that Σε/σ2 is a pseudo random X2 variate.) It is seen that the p obtained by setting S(p)=σ2 consistently results in p too small, confirming the theoretical results to this effect in [13]. We caution the reader that a good value of σ2 is required in order that the minimizer of Ř(p) be near that of R(p). In the computations, σ2 is taken as the variance used to generate pseudo random numbers ε.


<!-- p:19 -->


Fig. 3

Table 1. Inefficiencies associated with V, Ř and S

|             | a=0.1 - R (/~) min R (p) P   | a=0.01 - R (/~R) min R (p) P   | a=0.01 - R (/~s) min R (p) P   | a=0.01 - R (/~) min R (p) P   | R (/~R) min R P   | (p)     | R (/~s) min R (p) P   |
|-------------|------------------------------|--------------------------------|--------------------------------|-------------------------------|-------------------|---------|-----------------------|
| Example I   | 1.01                         | 1.00                           | 1.21                           | 1.02                          | 1.06              | 2.38    |                       |
| Example II  | 1.04                         | 1.10                           | 1.14                           | 1.01                          | 1.04              | 1.07    |                       |
| Example III | 1.42                         | 1.01                           | 2.02                           | 1.22                          | 1.00              | 2.06    |                       |
|             | a=0.001                      | a=0.001                        | a=0.001                        | a=0.001                       | a=0.001           | a=0.001 | a=0.001               |
| Example II  | 1.12                         | 1.04                           | 1.97                           |                               |                   |         |                       |

Letting p, ê and ês be the estimates of p using Generalized Cross-Validation, the minimizer of Ř(p), and Reinsch's suggestion respectively, the first three columns of the top of Table 1 gives the observed inefficiencies

$$\frac { R ( \hat { p } ) } { \min _ { p } R ( p ) } , \, \frac { R ( \hat { p } _ { R } ) } { \min _ { p } R ( p ) } \text { \ and \ } \frac { R ( \hat { p } _ { S } ) } { \min _ { p } R ( p ) } .$$

These experiments were replicated for σ= 0.01 and σ = 0.001. Plots of V, ê, R and S for the σ=0.01 case appear in Fig. 4, and the inefficiencies appear in the third through sixth columns of Table 1. The functions g and g, λ in the σ=0.01 case (which is roughly 1 % of the average g) are nearly visually indistinguishable and are not plotted. Good estimates of the derivative of g can be obtained by differentiating gn, λ. The functions g' and g', λ are plotted in Fig. 5, and it can be seen that at this signal to noise ratio the results are impressive. The mean square error R(p) in estimating the derivative,


<!-- p:20 -->

$$R _ { D } ( p ) = \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g ^ { \prime } \left ( \frac { j } { n } \right ) - g _ { n , \lambda } ^ { \prime } \left ( \frac { j } { n } \right ) \right ) ^ { 2 }$$

is also plotted in Fig.4. Note that the minimum of Rp(p) is close to the minimum of R(p), so that in these examples both the GCV estimate and the minimizer of Ř(p) are good from the point of view of minimizing Rp(p). This phenomena also obtained for the noisier data with σ=0.1, however the best derivative estimate with this 10% noise is fairly crude.


<!-- p:21 -->

As σ2 →0 R(p) will flatten out so that the optimum p → ∞, and Ř(p) and V(p) also display this behavior. To illustrate what can happen as σ2→0 we present Note that, while V(p) appears to have its minimum at p = ∞, R and Ř have finite minima. Judged from the point of view of inefficiency, however, ê and êr are not bad. The estimate ês becomes very inefficient in the σ2 small case (again agreeing with the theoretical results in [13], Eq. (1.3b) there says that as σ2 →0, Reinsch's suggestion becomes progressively worse).

### 6. Conclusions

The method of generalized cross validation has been shown both theoretically, and by example, to be an effective method for estimating that value of the spline smoothing parameter which minimizes the mean square error. Excellent estimates of the derivative are also obtained in examples involving roughly 1% and of 1% noise. 10

## Appendix

In this Appendix we give proofs of Lemmas 2.1 and 4.1 through 4.3.

Lemma 2.1. Q(s, t) given by

$$Q ( s , t ) = \sum _ { r = 0 } ^ { m } k _ { r } ( s ) \, k _ { r } ( t ) + ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( s , t )$$


<!-- p:22 -->


is the reproducing kernel for W(m) endowed with the inner product

$$\langle f , g \rangle = \sum _ { r = 0 } ^ { m - 1 } \left ( L _ { r } , f \right ) ( L _ { r } , g ) + \sum _ { 0 } ^ { 1 } f ^ { ( m ) } ( u ) \, g ^ { ( m ) } ( u ) \, d u .$$

Proof. Let Q(·)≡Q(t, ·). We have to show

$$\begin{array} { r l } & { i ) \ Q _ { t } \in W _ { 2 } ^ { ( m ) } \quad \text {for each } t } \\ & { i i ) \ \langle Q _ { t } , f \rangle = f ( t ) , \quad f \in W _ { 2 } ^ { ( m ) } , \ t \in [ 0 , 1 ] . } \end{array}$$

iods  dor ns e keis  o ts or and Wahba [7].) Part i) is obvious upon noting that Q, is a monospline of degree 2m and hence has 2m-2 continuous derivatives. To verify ii), we calculate

$$L _ { r } \, Q _ { t } = & k _ { r } ( t ) , \quad r = 0 , 1 , \dots , m - 1 \\ \frac { \partial m } { \partial u ^ { m } } \, Q _ { t } ( u ) = & k _ { m } ( t ) + ( - 1 ) ^ { 2 m - 1 } \, k _ { m } ( t , u )$$

and so

$$\langle Q _ { r } , f \rangle = & \sum _ { r = 0 } ^ { m - 1 } k _ { r } ( t ) ( L _ { r } , f ) + \int _ { 0 } ^ { 1 } ( k _ { m } ( t ) - k _ { m } ( t , u ) ) \, f ^ { ( m ) } ( u ) \, d u \\ = & \sum _ { r = 0 } ^ { m } k _ { r } ( t ) ( L _ { r } , f ) - \int _ { 0 } ^ { 1 } k _ { m } ( t , u ) \, f ^ { ( m ) } ( u ) \, d u \\ = & h ( t ) , \, \text { say.} \\ \intertext { w e w h o s w h o w } \intertext { W e w h o s w h o w }$$

We wish to show that h(t)≡ f(t). We are allowed to differentiate (A2.1) m—1 times under the integral sign, giving

$$h ^ { ( m ) } ( t ) = ( L _ { m } f ) - \frac { \partial } { \partial t } \int _ { 0 } ^ { 1 } k _ { 1 } ( t , u ) \, f ^ { ( m ) } ( u ) \, d u .$$

Since B1(t) =t − 1/2, k1(t, u) =(t −u) − 1/2, u &lt;t, =(t− u) + 1/2, u&gt;t, and hence, if t is a point of continuity of f(m),

$$t \text { is a point of community } 0 ^ { \prime } \text { } ; \\ h ^ { ( m ) } ( t ) = & ( L _ { m } f ) - \left [ \int _ { 0 } ^ { 1 } \frac { \partial } { \partial t } k _ { 1 } ( t , u ) \, f ^ { ( m ) } ( u ) \, d u + k _ { 1 } ( t , t _ { \_ } ) \, f ^ { ( m ) } ( t ) \\ & + \int _ { 0 } ^ { 1 } \frac { \partial } { \partial t } k _ { 1 } ( t , u ) \, f ^ { ( m ) } ( u ) \, d u - k _ { 1 } ( t , t _ { \_ } ) \, f ^ { ( m ) } ( t ) \right ] \\ = & ( L _ { m } f ) - \int _ { 0 } ^ { 1 } f ^ { ( m ) } ( u ) \, d u + f ^ { ( m ) } ( t ) \\ = & f ^ { ( m ) } ( t ) . \\ \intertext { t i s e y o s e t h a t L _ { r } ( f - h ) = 0 f r = 0 , 1 , \dots , m - 1 s o t h a t }$$

It is easy to see that L,(f−h)=0 for r=0,1, ...,m-1 so that f =h. (This lemma corrects an error in [13], p. 391, line 2.)


<!-- p:23 -->


Lemma 4.1. For any g∈ W(m),

$$b ^ { 2 } ( \lambda ) \equiv & \frac { 1 } { n } \| ( I - A ( \lambda ) ) \, g \| ^ { 2 } \leq \lambda \int _ { 0 } ^ { 1 } \left ( g ^ { ( m ) } ( u ) \right ) ^ { 2 } d u .$$

is the solution to the problem; Find f∈ Wm) to minimize * g,, z,  which

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g ( t _ { j } ) - f ( t _ { j } ) \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } d u .$$

Therefore,

$$\text {Here,} \\ \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g ( t _ { j } ) - g _ { n , \lambda } ^ { * } ( t _ { j } ) \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( g _ { n , \lambda } ^ { * } ( u ) \right ) ^ { 2 } \, d u \\ = \frac { 1 } { n } \left \| ( I - A ( \lambda ) ) \, g \right \| ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( g _ { n , \lambda } ^ { * } ( u ) \right ) ^ { 2 } \, d u \\ \leqq \frac { 1 } { n } \sum _ { j = 1 } ^ { n } \left ( g ( t _ { j } ) - g ( t _ { j } ) \right ) ^ { 2 } + \lambda \int _ { 0 } ^ { 1 } \left ( g ^ { ( m ) } ( u ) \right ) ^ { 2 } \, d u = \lambda \int _ { 0 } ^ { 1 } \left ( g ^ { ( m ) } ( u ) \right ) ^ { 2 } \, d u . \\ \text {Lemma 4.2. Let } \{ t _ { j } \} _ { i = 1 } ^ { n } \, \text {satisfy}$$

Lemma 4.2. Let {tin}i=1 ul satisfy

$$\int _ { 0 } ^ { t _ { n } } w ( u ) \, d u = i / n , \quad i = 1 , 2 , \dots , n , \ n = 1 , 2 , \dots$$

where w(u) is a strictly positive continuous weight function. Then if g(·)∉πm-1 1 (and not identically 0), and λ is bounded away from 0 as n→∞ then 一 g'(I n − A(λ))2 g is also bounded away from 0 as n→ ∞.

Proof. Let gn, be as in the proof of Lemma 4.1. Then converges in W{(m), as n→ ∞, to the minimizer, call it of i,

$$J _ { \infty , \, \mathfrak { g } } ( f ) = \int _ { 0 } ^ { 1 } \frac { ( g ( u ) - f ( u ) ) ^ { 2 } } { \omega ( u ) } \, d u + \lambda \int _ { 0 } ^ { 1 } \left ( f ^ { ( m ) } ( u ) \right ) ^ { 2 } \, d u .$$

Now if g∈πm-1, it is easy to see that g* =g, since, in that case J∞,g(g)=0. However, if g∉πm-1 then

$$J _ { \infty , \, g } ( \theta \, g ) < J _ { \infty , \, g } ( g )$$

lo

$$\text {for} \\ \theta = \frac { \int \frac { g ^ { 2 } ( u ) } { \omega ( u ) } d u } { \int \frac { g ^ { 2 } ( u ) } { \omega ( u ) } d u + \lambda \int g ^ { ( m ) } ( u ) \, d u } . \\$$

so that g is not equal to g. Furthermore


<!-- p:24 -->


```
P. Craven and G. Wahba
    _ = g' (I - A (lambda))^2 = _ = \sum _ { j = 1 } ^ { n } (g (t _ ) - g _ ^ { n } (t _ ) ) ^ { 2 } - \inf _ { j = 1 } ^ { ( g (u ) - g _ ^ { n } (u ) ) ^ { 2 } } \quad \text {for } \lambda > 0
    n

Lemma 4.3.  Let  {t _ } , f _ = 1,  satisfy  the  hypothesis  of  Lemma 4.2  with   0 < \alpha \leq w ( t )
  \leq \beta < \infty.  Then

      \frac { k _ { m } - + O ( \lambda ) + O ( 1 / n \lambda / 2 ) } { \beta ^ { 1 / 2 m } } \leq \frac { n \lambda ^ { 1 / 2 m } } { n } \left ( \frac { 1 } { n } T r \, A ( \lambda ) \right ) = n \lambda ^ { 1 / 2 m } \, \mu _ { 1 } ( \lambda )

      \leq \frac { k _ { m } - + O ( \lambda ) + O ( 1 / n \lambda / 2 m ) } { \beta ^ { 1 / 2 m } } \leq \frac { n \lambda ^ { 1 / 2 m } } { n } \left ( \frac { 1 } { n } T r \, A ^ { 2 } ( \lambda ) \right ) = n \lambda ^ { 1 / 2 m } \, \mu _ { 2 } ( \lambda )

      \leq \frac { l _ { m } - + O ( \lambda ) + O ( 1 / n \lambda / 2 m ) } { \alpha ^ { 1 / 2 m } }

as \lambda \to 0, n \lambda ^ { 1 / 2 m } \to \infty
where
      k _ { m } = \frac { 1 } { n } \int _ { \Omega _ { 0 } } \frac { 1 } { n } \int _ { \Omega _ { 0 } ^ { - 1 } } \frac { d x } { ( 1 + x ^ { 2 m } ) ^ { 2 } } .

Conversely,  if  n \lambda ^ { 1 / 2 m }  is  bounded  away  from  0  as  n \to \infty,  then  so  are  - Tr A ( \lambda )
        1
and  = Tr A ^ { 2 } ( \lambda).
      n
Proof.

      A ( \lambda ) = ( n \lambda + K ) M - 1 .

where

      M = K + n \lambda I

and

      P = M - ' T ( T ^ { M - 1 } T + A ) - 1 T .

Let
      n \hat { M } - 1 = E
            K M - 1 = A _ { 0 } .

Now,  since  0 < A _ { 0 } < A = A _ { 0 } + E < I,  ( where  B \prec C  means  C - B  is  non-negative
definite)  and  0 < E < I,  with  E  of  rank  m + 1,  we  have

      Tr A _ { 0 } \leq Tr A \leq Tr A _ { 0 } + ( m + 1 )
      Tr A _ { 0 } ^ { 2 } \leq Tr A ^ { 2 } - 2 Tr A _ { 0 } E + T r E ^ { 2 }

                      \leq T r A _ { 0 } ^ { 2 } + 3 T r E
                      \leq Tr A _ { 0 } ^ { 2 } + ( m + 1 )
```


<!-- p:25 -->


and so

$$\lambda ^ { 1 / 2 } \sum _ { \nu = 1 } ^ { n } \left ( \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + n \lambda } \right ) \leqq n \lambda ^ { 1 / 2 m } \left [ \frac { 1 } { n } \text {Tr} \, A ( \lambda ) \right ] \leqq \lambda ^ { 1 / 2 m } \sum _ { \nu = 1 } ^ { n } \left ( \frac { \lambda _ { \nu n } } { \lambda _ { \nu n } + n \lambda } \right ) + \hat { \lambda } ^ { 1 / 2 m } ( m + 1 ) ,$$

where λyn, v= 1, 2, ..., n, are the eigenvalues of K. We continue the proof under the assumption that the eigenvalues λy satisfy

$$\alpha \frac { ( \pi v ) ^ { 2 m } } { n } \leqq \lambda _ { v n } ^ { - 1 } \leqq \beta \frac { ( \pi v ) ^ { 2 m } } { n }$$

for some α, β, 0&lt;α≤β&lt;∞. Then we give an outline of an argument to show that the hypothesis of the theorem on {t} guarantees that (A4.3.1) holds with α, β given by

$$\alpha = & \min _ { t } w ( t ) ( 1 + o ( 1 ) ) \\ \beta = & \max _ { t } w ( t ) ( 1 + o ( 1 ) )$$

where o(1)→0 as n→ ∞. Using (A4.3.1) gives

$$\lambda ^ { 1 / 2 m } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \lambda \beta ( \pi v ) ^ { 2 m } ) } \leq \lambda ^ { 1 / 2 m } \sum _ { \nu = 1 } ^ { n } \left ( \frac { 1 } { 1 + n \lambda \lambda _ { \nu n } ^ { - 1 } } \right ) ^ { 2 } \leq \lambda ^ { 1 / 2 m } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \lambda \alpha ( \pi v ) ^ { 2 m } ) }$$

Since, for any fixed γ&gt;0 we have

$$( \mathfrak { m } - 1 ) ( \mathfrak { y } \lambda ) ^ { 1 / 2 m } \pi & = d x \\ \int _ { ( \mathfrak { y } \lambda ) ^ { 1 / 2 m } \pi } \frac { \int _ { ( 1 + x ^ { 2 m } ) ^ { 2 } } \leq ( \gamma \lambda ) ^ { 1 / 2 m } \pi \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \lambda \gamma ( \pi ) ^ { 2 m } \nu ^ { 2 m } ) ^ { 2 } } \leq \sum _ { 0 } ^ { \infty } \frac { d x } { ( 1 + x ^ { 2 m } ) ^ { 2 } } ,$$

we obtain

$$\frac { 1 } { \beta ^ { 1 / 2 m } \pi } \sum _ { ( \beta , \lambda ) ^ { 1 / 2 m } , \pi _ { m } } ^ { ( n - 1 ) ( \beta \lambda ) ^ { 1 / 2 m } } \frac { d x } { ( 1 + x ^ { 2 m } ) } \leq & n \lambda ^ { 1 / 2 m } \left [ \frac { 1 } { n } T r \, A ( \lambda ) \right ] \\ & \leq \frac { 1 } { \alpha ^ { 1 / 2 m } \pi } \int \frac { x } { 0 } \frac { d x } { ( 1 + x ^ { 2 m } ) ^ { 2 } } + \lambda ^ { 1 / 2 m } ( m + 1 ) ,$$

and so

$$\frac { k _ { m } } { \beta ^ { 1 / 2 m } } + O ( \lambda ) + O ( 1 / n \, \lambda ^ { 1 / 2 m } ) & \leqq n \, \lambda ^ { 1 / 2 m } \left [ \frac { 1 } { n } \, T r \, A ( \lambda ) \right ] \\ & \leqq \frac { k _ { m } } { \alpha ^ { 1 / 2 m } } + O ( \lambda ) + O ( 1 / n \, \lambda ^ { 1 / 2 m } ) .$$

A similar argument gives the inequality involving TrA2(λ). We now give a heuristic argument to show that A.4.3.1 holds with α, β given by A.4.3.2. The jkth entry Kjk of K is given (n even) by


<!-- p:26 -->


$$K _ { j k } = & ( - 1 ) ^ { m - 1 } \, k _ { 2 m } ( t _ { j } , t _ { k } ) = \sum _ { \substack { v = - \infty \\ v \neq 0 } } ^ { \infty } \frac { 1 } { ( 2 \pi \, v ) ^ { 2 m } } \, e ^ { 2 \pi i v ( t _ { j } - t _ { k } ) } \\ & \simeq \sum _ { \substack { v = - \infty \\ v \neq 0 } } ^ { n / 2 } \frac { 1 } { ( 2 \pi \, v ) ^ { 2 m } } \, e ^ { 2 \pi i v ( t _ { j } - t _ { k } ) } , \\ \intertext { a n d s o }$$

and so

K≈ΦDΦ*

1 where Φ is the n×n matrix with jvth entry e2πivtjn and D is a diagonal √n

matrix with vvth entry D, vv ≈ (2π v)2m) n v= −n/2, ..., n/2, v≠0, (n even). Since

1 tj+1,n−tjn , for some t ∈[t jn, t j+1,n] we have nw(t)'

$$\frac { 1 } { n } \sum _ { j = 1 } ^ { n } e ^ { 2 \pi i t _ { j } n } e ^ { - 2 \pi i \mu _ { j } n } \frac { 1 } { w ( t _ { j n } ) } \approx & \left \{ \int e ^ { 2 \pi i ( \nu - \mu ) s } d s = 1 , \quad \mu = v \\ = & 0 \quad \text {otherwise}$$

1 and so, letting D be the diagonal matrix with jjth entry we have w(t jn)'

Φ*DwΦ≈1.

Letting U = D 1/2 Φ, we have that U is (approximately) unitary w

$$K \approx D _ { w } ^ { - 1 / 2 } \ U D U ^ { * } D _ { w } ^ { - 1 / 2 } .$$

If equality were to hold in (A4.4.3) and U were unitary, then we would have that the eigenvalues λv of K satisfy

$$\min _ { t } \left ( \frac { 1 } { w ( t ) } \right ) D _ { v v } \leq \lambda _ { v n } \leq \max _ { t } \left ( \frac { 1 } { w ( t ) } \right ) D _ { v v } ,$$

$$\min _ { t } w ( t ) \, D _ { \nu \nu } \leqq \lambda _ { \nu \nu } ^ { - 1 } \leqq \max _ { t } w ( t ) \, D _ { \nu \nu } .$$

Since the 2vth and the 2v-1st largest Dvv are n we then would have (2πv)2m, (A4.3.1) with α, β as in (A4.3.2).

It remains to show that if 1/(n λ1/2m) is bounded below away from 0 as n→ ∞, 1 then so is −Tr A2(λ). We have n

$$\frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \beta \pi ^ { 2 m } \lambda v ^ { 2 m } ) ^ { 2 } } \leq & \frac { 1 } { n } T r \, A ^ { 2 } ( \lambda ) .$$

or Let λ= λ(n) satisfy n λ1/2m=c1/2m, equivalently λ= c/n2m. Then


<!-- p:27 -->


$$\frac { 1 } { ( 1 + \beta \pi ^ { 2 m } c ) ^ { 2 } } \leq & \frac { 1 } { n } \sum _ { \nu = 1 } ^ { n } \frac { 1 } { ( 1 + \beta \pi ^ { 2 m } c ( v ^ { 2 m } / n ^ { 2 m } ) ) ^ { 2 } } \leq & \frac { 1 } { n } T r \, A ^ { 2 } ( \lambda ) .$$

Acknowledgements. This work originated in the Common Room at the Oxford University Mathematical Institute, and the ministrations of the tea lady are remembered fondly by the American author (GW). She wishes to express her sincere appreciation for the hospitality of the Oxford University Mathematical Institute and St. Cross College, Oxford, and the support of the Science Research Council of Great Britain. We are grateful to Professor Gene Golub for several helpful discussions which led to the computational approach of Sect. 5.
