---
id: "Weinert-2007-efficient_whittaker_henderson_smoothing"
source_pdf: "../pdf/Weinert-2007-efficient_whittaker_henderson_smoothing.pdf"
source_filename: "Weinert-2007-efficient_whittaker_henderson_smoothing.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
references_file: "../references/Weinert-2007-efficient_whittaker_henderson_smoothing.references.md"
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
