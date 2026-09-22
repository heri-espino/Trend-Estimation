---
id: "18_L1_Trend_Filtering"
source_pdf: "../pdf/18_L1_Trend_Filtering.pdf"
source_filename: "18_L1_Trend_Filtering.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 100.0
visual_assets: "disabled"
references_file: "../references/18_L1_Trend_Filtering.references.md"
---

<!-- p:1 -->

## l1 Trend Filtering *

Seung-Jean Kim Kwangmoo Koh Stephen Boyd Dimitry Gorinevsky

Abstract. The problem of estimating underlying trends in time series data arises in a variety of disciplines. In this paper we propose a variation on Hodrick-Prescott (H-P) filtering, a widely used method for trend estimation. The proposed l1 trend filtering method substitutes a sum of absolute values (i.e., l1 norm) for the sum of squares used in H-P filtering to penalize variations in the estimated trend. The l1 trend filtering method produces trend estimates that are piecewise linear, and therefore it is well suited to analyzing time series with an underlying piecewise linear trend. The kinks, knots, or changes in slope of the estimated trend can be interpreted as abrupt changes or events in the underlying dynamics of the time series. Using specialized interior-point methods, l1 trend filtering can be carried out with not much more effort than H-P filtering; in particular, the number of arithmetic operations required grows linearly with the number of data points. We describe the method and some of its basic properties and give some illustrative examples. We show how the method is related to l1 regularization-based methods in sparse signal recovery and feature selection, and we list some extensions of the basic method.

Key words. detrending, l1 regularization, Hodrick-Prescott filtering, piecewise linear fitting, sparse signal recovery, feature selection, time series analysis, trend estimation

AMS subject classifications. 37M10, 62P99

DOI.10.1137/070690274

## 1. Introduction.

1.1. Trend Filtering. We are given a scalar time series yt, t = 1, . . . , n, assumed to consist of an underlying slowly varying trend xt and a more rapidly varying random component zt. Our goal is to estimate the trend component xt or, equivalently, estimate the random component zt = yt − xt. This can be considered as an optimization problem with two competing objectives: We want xt to be smooth, and we want zt (our estimate of the random component, sometimes called the residual) to be small. In some contexts, estimating xt is called smoothing or filtering.

Trend filtering comes up in several applications and settings including macroeconomics (e.g., [52, 86]), geophysics (e.g., [1, 8, 9]), financial time series analysis (e.g., [97]), social sciences (e.g., [66]), revenue management (e.g., [91]), and biological and medical sciences (e.g., [43, 68]). Many trend filtering methods have been proposed, including Hodrick–Prescott (H-P) filtering [52, 64], moving average filtering [75], exponential smoothing [70], bandpass filtering [21, 4], smoothing splines [81], de-trending via rational square-wave filters [79], a jump process approach [106], median filtering [101], a linear programming (LP) approach with fixed kink points [72], and wavelet transform analysis [23]. (All these methods except for the jump process approach, the LP approach, and median filtering are linear filtering methods; see [4] for a survey of linear filtering methods in trend estimation.) The most widely used methods are moving average filtering, exponential smoothing, and H-P filtering, which is especially popular in economics and related disciplines due to its application to business cycle theory [52]. The idea behind H-P filtering can be found in several fields and can be traced back at least to work in 1961 by Leser [64] in statistics.

*Received by the editors May 2, 2007; accepted for publication (in revised form) May 28, 2008; published electronically May 4, 2009. This work was funded in part by the Precourt Institute on Energy Efficiency, by Army award W911NF-07-1-0029, by NSF award 0529426, by NASA award NNX07AEIIA, by AFOSR award FA9550-06-1-0514, and by AFOSR award FA9550-06-1-0312.

http://www.siam.org/journals/sirev/51-2/69027.html

Information Systems Laboratory, Electrical Engineering Department, Stanford University, Stanford, CA 94305-9510 (sjkim@stanford.edu, deneb1@stanford.edu, boyd@stanford.edu, gorin@ stanford.edu).


<!-- p:2 -->


1.2. l1 Trend Filtering. In this paper we propose l1 trend filtering, a variation on H-P filtering which substitutes a sum of absolute values (i.e., an l1 norm) for the sum of squares used in H-P filtering to penalize variations in the estimated trend. (The term "filtering" is used in analogy with "H-P filtering." Like H-P filtering, l1 trend filtering is a batch method for estimating the trend component from the whole history of observations.)

We will see that the proposed l1 trend filter method shares many properties with the H-P filter and has the same (linear) computational complexity. The principal difference is that the l1 trend filter produces trend estimates that are smooth in the sense of being piecewise linear. The l1 trend filter is thus well suited to analyzing time series with an underlying piecewise linear trend. The kinks, knots, or changes in slope of the estimated trend can be interpreted as abrupt changes or events in the underlying dynamics of the time series; the l1 trend filter can be interpreted as detecting or estimating changes in an underlying linear trend. Using specialized interior-point methods, l1 trend filtering can be carried out with not much more effort than H-P filtering; in particular, the number of arithmetic operations required grows linearly with the number of data points.

1.3. Outline. In the next section we set up our notation and give a brief summary of H-P filtering, listing some properties for later comparison with our proposed l1 trend filter. The l1 trend filter is described in section 3 and compared to the H-P filter. We give some illustrative examples in section 4.

In section 5 we give the optimality condition for the underlying optimization problem that defines the l1 trend filter, and we use it to derive some of the properties given in section 3. We also derive a Lagrange dual problem that is interesting on its own and is also used in a primal-dual interior-point method we describe in section 6. We list a number of extensions of the basic idea in section 7.

2. Hodrick-Prescott Filtering. In H-P filtering, the trend estimate xt is chosen to minimize the weighted sum objective function

$$( 1 ) \quad ( 1 / 2 ) \sum _ { t = 1 } ^ { n } ( y _ { t } - x _ { t } ) ^ { 2 } + \lambda \sum _ { t = 2 } ^ { n - 1 } ( x _ { t - 1 } - 2 x _ { t } + x _ { t + 1 } ) ^ { 2 } ,$$

where λ ≥ 0 is the regularization parameter used to control the trade-off between smoothness of xt and the size of the residual yt − xt. The first term in the objective function measures the size of the residual; the second term measures the smoothness of the estimated trend. The argument appearing in the second term, xt−1 −2xt + xt+1, is the second difference of the time series at time t; it is zero when and only when the three points xt-1, xt, xt+1 are on a line. The second term in the objective is zero if and only if xt is affine, i.e., has the form xt = α + βt for some constants α and β. (In other words, the graph of xt is a straight line.) The weighted sum objective (1) is strictly convex and coercive in x, and so has a unique minimizer, which we denote xhp.


<!-- p:3 -->


We can write the objective (1) as

$$( 1 / 2 ) \| y - x \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 2 } ^ { 2 } ,$$

where x = (x1, . . . , xn) ∈ Rn, y = (y1, . . , yn) ∈ Rn, u||2 = (Σi u2)1/2 is the Euclidean or l2 norm, and D ∈ R(n-2)×n is the second-order difference matrix

$$1 -2 1 1 -2 1 (2) D = 1-2 1 1 -2 1$$

(D is Toeplitz with first row [ 1 −2 1 0 . .. 0 ]; entries not shown above are zero.) The H-P trend estimate is

$$x ^ { h p } = ( I + 2 \lambda D ^ { T } D ) ^ { - 1 } y .$$

H-P filtering is supported in several standard software packages for statistical data analysis, e.g., SAS, R, and Stata.

We list some basic properties of H-P filtering, which we refer to later when we compare it to our proposed trend estimation method.

- Linear computational complexity. The H-P estimated trend xhp in (3) can be computed in O(n) arithmetic operations, since D is tridiagonal.
- Linearity. From (3) we see that the H-P estimated trend xhp is a linear function of the time series data y.
- Convergence to original data as λ → 0. The relative fitting error satisfies the inequality

$$( 4 ) & & \frac { \| y - x ^ { h p } \| _ { 2 } & \leq \frac { 3 2 \lambda } { 1 + 3 2 \lambda } .$$

This shows that as the regularization parameter λ decreases to zero, xhp converges to the original time series data y.

- Convergence to best affine fit as λ → ∞. As λ → ∞, the H-P estimated trend converges to the best affine (straight-line) fit to the time series data,

$$x ^ { b a } = \alpha ^ { b a } + \beta ^ { b a } t ,$$

with intercept and slope

$$\alpha ^ { b a } & = \frac { \sum _ { t = 1 } ^ { n } t ^ { 2 } \sum _ { t = 1 } ^ { n } y _ { t } - \sum _ { t = 1 } ^ { n } t \sum _ { t = 1 } ^ { n } t y _ { t } } { n \sum _ { t = 1 } ^ { n } t ^ { 2 } - ( \sum _ { t = 1 } ^ { n } t ) ^ { 2 } } , \\ \beta ^ { b a } & = \frac { n \sum _ { t = 1 } ^ { n } t y _ { t } - \sum _ { t = 1 } ^ { n } t \sum _ { t = 1 } ^ { n } y _ { t } } { n \sum _ { t = 1 } ^ { n } t ^ { 2 } - ( \sum _ { t = 1 } ^ { n } t ) ^ { 2 } } .$$


<!-- p:4 -->


- Commutability with affine adjustment. We can change the order of H-P filtering and affine adjustment of the original time series data, without affect: For ay α ad β, the H-P trend estimate of the time series data  ̄t = yt − α − βt is τhp xt with α = αba, β = βba, which corresponds to subtracting the best affine fit from the original data.)
- Regularization path. The H-P trend estimate xhp is a smooth function of the regularization parameter λ, as it varies over [0, ∞). As λ decreases to zero, xhp converges to the original data y; as λ increases, xhp becomes smoother, and converges to xba, the best affine fit to the time series data.

We can derive the relative fitting error inequality (4) as follows. From the optimality condition y − xhp = λDT Dxhp we obtain

$$y - x ^ { h p } = 2 \lambda D ^ { T } D ( I + 2 \lambda D ^ { T } D ) ^ { - 1 } y .$$

The spectral norm of D is no more than 4:

$$\| D x \| _ { 2 } = \| x _ { 1 \colon n - 2 } - 2 x _ { 2 \colon n - 1 } + x _ { 3 \colon n } \| _ { 2 } \leq \| x _ { 1 \colon n - 2 } \| _ { 2 } + 2 \| x _ { 2 \colon n - 1 } \| _ { 2 } + \| x _ { 3 \colon n } \| _ { 2 } \leq 4 \| x \| _ { 2 } ,$$

where xi:j = (xi, · . . , xj). The eigenvalues of DT D lie between 0 and 16, so the eigenvalues of 2λDT D(I + 2λDT D)−1 lie between 0 and 32λ/(1 + 32λ). It follows that

$$\| y - x ^ { h p } \| _ { 2 } \leq ( 3 2 \lambda / ( 1 + 3 2 \lambda ) ) \| y \| _ { 2 } .$$

3. l1 Trend Filtering. We propose the following variation on H-P filtering, which we call l1 trend filtering. We choose the trend estimate as the minimizer of the weighted sum objective function

$$( 5 ) \quad ( 1 / 2 ) \sum _ { t = 1 } ^ { n } ( y _ { t } - x _ { t } ) ^ { 2 } + \lambda \sum _ { t = 2 } ^ { n - 1 } | x _ { t - 1 } - 2 x _ { t } + x _ { t + 1 } | ,$$

which can be written in matrix form as

$$( 1 / 2 ) \| y - x \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 1 } ,$$

where ∥u∥|1 = Σi |ui| denotes the l1 norm of the vector u. As in H-P filtering, λ is a nonnegative parameter used to control the trade-off between smoothness of x and size of the residual. The weighted sum objective (1) is strictly convex and coercive in x and so has a unique minimizer, which we denote xlt. (The superscript "lt" stands for "l1 trend.")

We list some basic properties of l1 trend filtering, pointing out similarities and differences with H-P filtering.

- Linear computational complexity. There is no analytic formula or expression for xlt, analogous to (3). But like xhp, xlt can be computed numerically in O(n) arithmetic operations. (We describe an efficient method for computing xlt in section 6. Its worst-case complexity is O(n1.5), but practically its computational effort is linear in n.)
- Nonlinearity. The l1 trend estimate xlt is not a linear function of the original data y. (In contrast, xhp is a linear function of y.)


<!-- p:5 -->


- Convergence to original data as λ → 0. The maximum fitting error satisfies the bound

$$\| y - x ^ { l t } \| _ { \infty } \leq 4 \lambda ,$$

where ∥u∥|∞ = maxi |ui| denotes the l∞ norm of the vector u. (Cf. the analogous bound for H-P trend estimation, given in (4).) This implies that x t → y as λ → 0.

- Finite convergence to best affine fit as λ → ∞. As in H-P filtering, xlt → xba as λ → ∞. For l1 trend estimation, however, the convergence occurs for a finite value of λ,

$$\lambda _ { \max } = \| ( D D ^ { T } ) ^ { - 1 } D y \| _ { \infty } .$$

For λ ≥ λmax, we have xlt = xba. (In contrast, xhp → xba only in the limit as λ → ∞.) This maximum value λmax is readily computed with O(n) arithmetic steps. (The derivation is given in section 5.1.)

- Commutability with affine adjustment. As in H-P filtering, we can swap the order of affine adjustment and trend filtering, without affect.
- Piecewise-linear regularization path. The l1 trend estimate xlt is a piecewiselinear function of the regularization parameter λ, as it varies over [0, ∞): There are values λ1 , . . . , λk, with 0 = λk &lt; · . . &lt; λ1 = λmax, for which

$$x ^ { l t } = \frac { \lambda _ { i } - \lambda } { \lambda _ { i } - \lambda _ { i + 1 } } x ^ { ( i + 1 ) } + \frac { \lambda - \lambda _ { i + 1 } } { \lambda _ { i } - \lambda _ { i + 1 } } x ^ { ( i ) } , \ \lambda _ { i + 1 } \leq \lambda \leq \lambda _ { i } , \ \ i = 1 , \dots , k - 1 ,$$

where x(i) is x1t with λ = λi. (So x(1) = xba, x(k) = y.)

- Linear extension property. Let xlt denote the l1 trend estimate for (y1, . . . , Yn+1). There is an interval [l, u], with l &lt; u, for which

$$\tilde { x } ^ { l t } = ( x ^ { l t } , 2 x _ { n } ^ { l t } - x _ { n } ^ { l }$$

provided yn+1 ∈ [u, l]. In other words, if the new observation is inside an interval, the l1 trend estimate linearly extends the last affine segment.

- 3.1. Piecewise Linearity. The basic reason the l1 trend estimate xlt might be preferred over the H-P trend estimate xhp is that it is piecewise linear in t: There are (integer) times 1 = t1 &lt; t2 &lt; · · · &lt; tp−1 &lt; tp = n for which

$$x _ { t } ^ { \text {lt} } = \alpha _ { k } + \beta _ { k } t , \ \ t _ { k } \leq t \leq t _ { k + 1 } , \ \ k = 1 , \dots , p - 1 .$$

In other words, over each (integer) interval [ti, ti+1], xlt is an affine function of t. We can interpret αk and βk as the local intercept and slope in the kth interval. These local trend parameters are not independent: they must give consistent values for xlt at the join or kink points, i.e.,

$$\alpha _ { k } + \beta _ { k } t _ { k + 1 } = \alpha _ { k + 1 } + \beta _ { k + 1 } t _ { k + 1 } , \ \ k = 1 , \dots , p - 1 .$$

The points t2, . . . , tp-1 are called kink points. We say that xlt is piecewise linear with p − 2 kink points. (The kink point tk can be eliminated if αk = αk−1, so we generally assume that αk ≠ αk−1.)

In one extreme case, we have p = 2, which corresponds to no kink points. In this case t1 = 1, t2 = n, and xlt = xba is affine. In the other extreme case, there is a kink at every time point: we have ti = i, i = 1, . . . , p = n. In this case the piecewise linear form (8) is vacuous; it imposes no constraints on xlt. This corresponds to λ = 0, and x1t = y.


<!-- p:6 -->


The kink points correspond to changes in slope of the estimated trend and can be interpreted as abrupt changes or events in the underlying dynamics of the time series. The number of kinks in xlt typically decreases as the regularization parameter increases, but counterexamples show this need not happen.

Piecewise linearity of the trend estimate is not surprising: It is well known when an l1 norm term is added to an objective to be minimized, or constrained, the solution typically has the argument of the l1 norm term sparse (i.e., with many zero elements). In this context, we would predict that Dx (the second-order difference of the estimated trend) will have many zero elements, which means that the estimated trend is piecewise linear.

The general idea of l1 regularization for the purposes of sparse signal recovery or feature selection has been used in geophysics since the early 1970s; see, e.g., [22, 67, 92]. In signal processing, the idea of l1 regularization comes up in several contexts, including basis pursuit (denoising) [19, 20], image decomposition [31, 88], signal recovery from incomplete measurements [17, 16, 26, 27, 96], sensor selection [55], fault identification [108], and wavelet thresholding [28]. In statistics, the idea of l1 regularization is used in the well-known Lasso algorithm [93] for l1-regularized linear regression, its extensions such as the fused Lasso [94], the elastic net [107], the group Lasso [105], and the monotone Lasso [51], and l1-regularized logistic regression [61, 62, 77]. The idea of l1 regularization has been used in other contexts, including portfolio optimization [69], control design [48], computer-aided design of integrated circuits [13], decoding of linear codes [15], and machine learning (sparse principal ] os t red  l] snt ndso)

We note that l1 trend filtering is related to segmented regression, a statistical regression method in which the variables are segmented into groups and regression analysis is performed on each segment. Segmented regression arises in a variety of contexts, including abrupt change detection and time series segmentation (especially as a preprocessing step for mining time series databases); the reader is referred to a survey [57] and the references therein. There are two types of time series segmentation. One does not require the fits for two consecutive segments to have consistent values at their join point; see, e.g., [71, 63, 87, 80, 102]. The other requires the fits for two consecutive segments to be consistent at their join point, which is often called joinpoint regression; see, e.g., [32, 35, 36, 58, 89, 104]. We can think of l1 trend filtering as producing a segmented linear regression, with an affine fit on each segment, and with consistent values at the join points. In l1 trend filtering, the segmentation and the affine fit on each segment are found by solving one optimization problem.

In time series segmentation, we can use the principle of dynamic programming (DP) to find the best fit that minimizes the fitting error among all functions that consist of k affine segments, with or without the requirement of consistency at the join points. In an early paper [5, 6], Bellman showed how DP can be used for segmented linear regression without the requirement of consistency at the join points. The DP arst t ht ] n n (   t  t t  thm with the consistency requirement at the join points is, however, far more involved than in the case when it is absent. As a heuristic, l1 trend filtering produces a segmented linear regression in O(n) arithmetic operations. Another heuristic based on grid search is described in [58], and an implementation, called the Joinpoint Regression Program, is available from http://srab.cancer.gov/joinpoint/.


<!-- p:7 -->


3.2. l1 Trend Filtering and Sparse Approximation. To see the connection between l1 trend filtering and l1 regularization-based sparse approximation more clearly, we note that the l1 trend filtering problem is equivalent to the l1-regularized least squares problem:

$$( 9 ) \quad \minimize _ { i = 3 } \ ( 1 / 2 ) \| A \theta - y \| _ { 2 } ^ { 2 } + \lambda \sum _ { i = 3 } ^ { n } | \theta _ { i } | ,$$

where θ = (θ1, . . . , θn) ∈ Rn is the variable and A is the lower triangular matrix

1


2

1

A =

∈Rn×n.

1

3

2

1

1 n −1 n −2 . 2 1

The solution θlt to this problem and the l1 trend estimate are related by

$$( 1 0 ) ^ { ( 1 0 ) } = A \theta ^ { 1 t } .$$

We can give a simple interpretation of the coefficients: θ1t is the offset (θ1t = x1t), − x1), and for t ≥ 3, θt is the second-order difference of x at t − 1 (θt = (Dxlt)t−2). This interpretation shows again the equivalence between the l1 trend filtering problem and the l1-regularized least squares problem (9). (This interpretation also shows that l1 trend filtering is a special type of basis pursuit denoising [20] and is related to multivariate adaptive regression splines (MARS) [37, 49, 50] that use truncated linear functions as basis functions.)

From a standard result in l1-regularized least squares [30, 83], the solution θlt to (9) is a piecewise-linear function of the regularization parameter λ, as it varies over [0, ∞). From (10), we can see that the regularization path of l1 trend filtering is piecewise linear.

4. Illustrative Examples. Our first example uses synthetic data, generated as

$$y _ { t } = x _ { t } + z _ { t } , \ \ t = 1 , \dots , n , \quad x _ { t + 1 } = x _ { t } + v _ { t } , \ \ t = 1 , \dots , n - 1 ,$$

with initial condition x1 = 0. Here xt is the "true" underlying trend, zt is the irregular component or noise, and vt is the trend slope. The noises zt are IID N(0, σ2). The trend slopes vt are chosen from a simple Markov process (independent of z). With probability p, we have vt+1 = vt, i.e., no slope change in the underlying trend. (Thus, the mean time between slope changes is 1/(1 − p).) With probability 1 − p, we choose vt+1 from a uniform distribution on [-b, b]. We choose the initial slope v1 from a uniform distribution on [-b, b]. The change in xt between two successive changes in slope is given by the product of two independent random variables: the time between changes (which is geometrically distributed with mean 1/(1 - p)) and the slope (which is uniform over [−b, b]). It has zero mean and variance (1 + p)(1 − p)−2b2/3. The standard deviation of the change in xt between successive changes in slope is thus √(1 + p)/3(b/(1 − p)).


<!-- p:8 -->


For our example, we use the parameter values

$$n = 1 0 0 0 , \quad p = 0 . 9 9 , \quad \sigma = 2 0 , \quad b = 0 . 5 .$$

Thus, the mean time between slope changes is 100, and the standard deviation of the change in xt between slope changes is 40.7. The particular sample we generated had 8 changes in slope.

The l1 trend estimates were computed using two solvers: cvx [42], a MATLABbased modeling system for convex optimization (which calls SDPT3 [95] or SeDuMi [90], a MATLAB-based solver for convex problems), and a C implementation of the specialized primal-dual interior-point method described in section 6. The run times on a 3GHz Pentium IV were around a few seconds and 0.01 seconds, respectively.

The results are shown in Figure 1. The top left plot shows the true trend xt, and the top right plot shows the noise corrupted time series yt. In the middle left plot, we show xlt for λ = 35000, which results in 4 kink points in the estimated trend. The middle right plot shows the H-P trend estimate with λ adjusted to give the same fitting error as xlt, i.e., ∥y − xlt∥2 = ∥y − xhp∥2. Even though xlt is not a particularly good estimate of xt, it has identified some of the slope change points fairly well. The bottom left plot shows xlt for λ = 5000, which yields 7 kink points in xlt. The bottom right plot shows xhp, with the same fitting error. In this case the estimate of the underlying trend is quite good. Note that the trend estimation error for xlt is better than xhp, especially around the kink points.

Our next example uses real data, 2000 consecutive daily closing values of the S&amp;P 500 Index, from March 25, 1999, to March 9, 2007, after logarithmic transform. The data are shown in the top plot of Figure 2. In the middle plot, we show xlt for λ = 100, which results in 8 kink points in the estimated trend. The bottom plot shows the H-P trend estimate with the same fitting error.

In this example (in contrast to the previous one) we cannot say that the l1 trend estimate is better than the H-P trend estimate. Each of the two trend estimates is a smoothed version of the original data; by construction, they have the same l2 fitting error. If for some reason you believe that the (log of the) S&amp;P 500 Index is driven by an underlying trend that is piecewise linear, you might prefer the l1 trend estimate over the H-P trend estimate.

## 5. Optimality Condition and Dual Problem.

5.1. Optimality Condition. The objective function (5) of the l1 trend filtering problem is convex but not differentiable, so we use a first-order optimality condition based on subdifferential calculus. We obtain the following necessary and sufficient condition for x to minimize (5): there exists ν ∈ Rn such that

$$y - x = D ^ { T } \nu , \quad \nu _ { t } \in \left \{ \begin{array} { c c c } \{ + \lambda \} , & ( D x ) _ { t } > 0 , \\ \{ - \lambda \} , & ( D x ) _ { t } < 0 , & t = 1 , \dots , n - 2 . \\ [ - \lambda , \lambda ] , & ( D x ) _ { t } = 0 , \end{array}$$

(Here, we use the chain rule for subdifferentials: If f is convex, then the subdifferential [4 ·d 2]   ( + x)fx = (x) q  s ( + x)f = (x) or [10, Chap. 2] for more on subdifferential calculus.) Since DDT is invertible, the optimality condition (12) can be written as

$$( ( D D ^ { T } ) ^ { - 1 } D ( y - x ) ) _ { t } \in \left \{ \begin{array} { l l } { \{ + \lambda \} , } & { ( D x ) _ { t } > 0 , } \\ { \{ - \lambda \} , } & { ( D x ) _ { t } < 0 , } & { t = 1 , \dots , n - 2 . } \\ { [ - \lambda , \lambda ] , } & { ( D x ) _ { t } = 0 , } \end{array}$$


<!-- p:9 -->


Fig. I Trend estimation on synthetic data. Top left: The true trend xt. Top right: Observed time series data yt. Middle left: l1 trend estimate x1t with four total kinks (λ = 35000). Middle right: H-P trend estimate xhp with same fitting error. Bottom left: xlt with seven total kinks (λ = 5000). Bottom right: H-P trend estimate xhp with same fitting error.

40


0

-40


y

-80


-120


0

200

400

600

800

1000

0

200

400

600

800

1000

40


0

1二

40

jqx

40

-80


-120


0

200

400

600

800

1000

0

200

400

600

800

1000

40


-80


-120


0

200

400

600

800

1000

0

200

400

600

800

1000

t


The maximum fitting error bound in (6) follows from the optimality condition above. For any ν ∈ Rn−2 with νt ∈ [−λ, λ],

$$- 4 \lambda \leq ( D ^ { T } \nu ) _ { t } \leq 4 \lambda , \quad t = 1 , \dots , n .$$

It follows from (12) that the minimizer x of (5) satisfies

$$- 4 \lambda \leq x _ { t } - y _ { t } \leq 4 \lambda , \quad t = 1 , \dots , n .$$


<!-- p:10 -->


Fig. 2 Trend estimation results for the S&amp;P 500 Index for the period of March 25, 1999, to March 9, 2007. Top: Original data. Middle: l1 trend estimate xlt for λ = 100. Bottom: H-P trend estimate xhp with same fitting error.

7.3

7.2

log-price

7.1

7.0

6.9

6.8

6.7

1/2000

1/2002

1/2004

1/2006

7.3

7.2

log-price

7.1

7.0

6.9

6.8

6.7

1/2000

1/2002

1/2004

1/2006

7.3

7.2

AN

log-price

7.1

7.0

6.9

6.8

6.7

1/2000

1/2002

1/2004

1/2006

We can now derive the formula (7) for λmax. Since xba is affine, Dxba = 0, so the condition that xba is optimal is that ((DDT)−1D(y − xba))t ∈ [−λ, λ] for t = 1, . . . , n − 2, i.e.,

$$\| ( D D ^ { T } ) ^ { - 1 } D ( y - x ^ { b a } ) \| _ { \infty } = \| ( D D ^ { T } ) ^ { - 1 } D y \| _ { \infty } \leq \lambda .$$


<!-- p:11 -->


We can use the optimality condition (12) to see whether the linear extension property holds for a new observation yn+1. From the optimality condition (12), we can see that if yn+1 satisfies

$$2 x _ { n } ^ { l t } - x _ { n - 1 } ^ { l t } \, \right ] \right ) \right \| _ { \infty } \leq \lambda ,$$

where D ∈ R(n-1)×(n+1) is the second-order difference matrix on Rn+1, then the inequality, we can easily find the bounds l and u such that if l ≤ yn+1 ≤ u, then the linear extension property holds.

5.2. Dual Problem. To derive a Lagrange dual of the primal problem of minimizing (5), we first introduce a new variable z ∈ Rn-2, as well as a new equality constraint z = Dx, to obtain the equivalent formulation

$$\begin{array} { r l } { \minimize } & ( 1 / 2 ) \| y - x \| _ { 2 } ^ { 2 } + \lambda \| z \| _ { 1 } } \\ { \subtext {subject to } } & z = D x . } \end{array}$$

Associating a dual variable ν ∈ Rn-2 with the equality constraint, the Lagrangian is

$$L ( x , z , \nu ) = ( 1 / 2 ) \| y - x \| _ { 2 } ^ { 2 } + \lambda \| z \| _ { 1 } + \nu ^ { T } ( D x - z ) .$$

The dual function is

$$\inf _ { x , z } L ( x , z , \nu ) = \left \{ \begin{array} { c c c } - ( 1 / 2 ) \nu ^ { T } D D ^ { T } \nu + y ^ { T } D ^ { T } \nu , & - \lambda 1 \leq \nu \leq \lambda 1 , \\ - \infty & \text {otherwise.} \end{array}$$

The dual problem is

$$\min \min i t s _ { \substack { \minimize \quad g ( \nu ) = ( 1 / 2 ) \nu ^ { T } D D ^ { T } \nu - y ^ { T } D ^ { T } \nu \\ \text {subject to } - \lambda 1 \leq \nu \leq \lambda 1 . }$$

(Here a ≤ b means ai ≤ bi for all i.) The dual problem (13) is a (convex) quadratic program (QP) with variable ν ∈ Rn−2. We say that ν ∈ Rn−2 is strictly dual feasible if it satisfies −λ1 &lt; ν &lt; λ1.

From the solution νlt of the dual (13), we can recover the l1 trend estimate via

$$x ^ { \text {lt} } = y - D ^ { T } \nu ^ { \text {lt} } .$$

6. A Primal-Dual Interior-Point Method. The QP (13) can be solved by standrr  d -d ns dds  nttod  od 74, 103] and more specialized methods such as path following [76, 30]. These methods can exploit the special structure of the problem, i.e., the bandedness of the quadratic form in the objective, to solve the problem very efficiently. To see how this can be done, we describe a simple primal-dual method in this section. For more detail on these (and related) methods, see, e.g., [12, section 11.7] or [103].

The worst-case number of iterations in primal-dual interior-point methods for the QP (13) is O(n1/2) [73]. In practice, primal-dual interior-point methods solve QPs in a number of iterations that is just a few tens, almost independent of the problem size or data. Each iteration is dominated by the cost of computing the search direction, which, if done correctly for the particular QP (13), is O(n). It follows that the overall complexity is O(n), the same as for solving the H-P filtering problem (but with a larger constant hidden in the O(n) notation).


<!-- p:12 -->


The search direction is the Newton step for the system of nonlinear equations

$$r _ { t } ( \nu , \mu _ { 1 } , \mu _ { 2 } ) = 0 ,$$

where t &gt; 0 is a parameter and

$$( 1 6 ) \ \ r _ { t } ( \nu , \mu _ { 1 } , \mu _ { 2 } ) = \left [ \begin{array} { c } \ r _ { d u a l } \\ \ r _ { c e n t } \end{array} \right ] = \left [ \begin{array} { c } \nabla g ( \nu ) + D ( \nu - \lambda 1 ) ^ { T } \mu _ { 1 } - D ( \nu + \lambda 1 ) ^ { T } \mu _ { 2 } \\ - \mu _ { 1 } ( \nu - \lambda 1 ) + \mu _ { 2 } ( \nu + \lambda 1 ) - ( 1 / t ) 1 \end{array} \right ]$$

is the residual. (The first component is the dual feasibility residual, and the second is the centering residual.) Here μ1, μ2 ∈ Rn-2 are (positive) dual variables for the inequality constraints in (13), and ν is strictly dual feasible. As t → ∞, rt(ν, μ1, μ2) = .(   r o ( --s   sos e idea is to take Newton steps for solving the set of nonlinear equations rt(ν, μ1, μ2) = 0 for a sequence of increasing values of t.

The Newton step is characterized by

$$r _ { t } ( \nu + \Delta \nu , \mu _ { 1 } + \Delta \mu _ { 1 } , \mu _ { 1 } + \Delta \mu _ { 1 } ) \approx r _ { t } ( \nu , \mu _ { 1 } , \mu _ { 2 } ) + D r _ { t } ( \nu , \mu _ { 1 } , \mu _ { 2 } ) ( \Delta \nu , \Delta \mu _ { 1 } , \Delta \mu _ { 2 } ) = 0 ,$$

where Drt is the derivative (Jacobian) of rt. This can be written as

$$\left [ \begin{array} { c c c } \ D D ^ { T } & I & - I \\ I & J _ { 1 } & 0 \\ - I & 0 & J _ { 2 } \end{array} \right ] \left [ \begin{array} { c } \Delta \nu \\ \Delta \mu _ { 1 } \\ \Delta \mu _ { 2 } \end{array} \right ] = - \left [ \begin{array} { c } \ D D ^ { T } z - D y + \mu _ { 1 } - \mu _ { 2 } \\ f _ { 1 } + ( 1 / t ) \, \text {diag} ( \mu _ { 1 } ) ^ { - 1 } 1 \\ f _ { 2 } + ( 1 / t ) \, \text {diag} ( \mu _ { 2 } ) ^ { - 1 } 1 \end{array} \right ] ,$$

where

$$f _ { 1 } & = \nu - \lambda 1 \in R ^ { n - 2 } , \\ f _ { 2 } & = - \nu - \lambda 1 \in R ^ { n - 2 } , \\ J _ { i } & = d iag ( \mu _ { i } ) ^ { - 1 } \, d iag ( f _ { i } ) \in R ^ { ( n - 2 ) \times ( n - 2 ) } .$$

(Here diag(w) is the diagonal matrix with diagonal entries w.) By eliminating (∆μ1, ∆μ2), we obtain the reduced system

$$( D D ^ { T } - J _ { 1 } ^ { - 1 } J _ { 2 } ^ { - 1 } ) \, \Delta \nu = - \left ( D D ^ { T } \nu - D y - ( 1 / t ) \, \text {diag} ( f _ { 1 } ) ^ { - 1 } 1 + ( 1 / t ) \, \text {diag} ( f _ { 2 } ) ^ { - 1 } 1 \right ) .$$

The matrix DDT — J−1 J−1 is banded (with bandwidth 5) so we can solve this reduced system in O(n) arithmetic operations. The other two components of the search step, ∆μ1 and ∆μ2, can be computed as

$$\Delta \mu _ { 1 } & = - \left ( \mu _ { 1 } + ( 1 / t ) \, d i a g ( f _ { 1 } ) ^ { - 1 } 1 + J _ { 1 } ^ { - 1 } d \nu \right ) , \\ \Delta \mu _ { 2 } & = - \left ( \mu _ { 2 } + ( 1 / t ) \, d i a g ( f _ { 2 } ) ^ { - 1 } 1 - J _ { 2 } ^ { - 1 } d \nu \right )$$

in O(n) arithmetic operations (since the matrices J1 and J2 are diagonal).

A C implementation of a primal-dual interior-point method for l1 trend filtering is available online from www.stanford.edu/~boyd/11\_tf. For a typical problem with n = 10000 data points, it computes xlt in around one second on a 3GHz Pentium IV. Problems with one million data points require around 100 seconds, consistent with linear computational complexity in n.


<!-- p:13 -->


7. Extensions and Variations. The basic l1 trend estimation method described above can be extended in many ways, some of which we describe here. In each case, the computation reduces to solving one or a few convex optimization problems, and so is quite tractable; the interior-point method described above is readily extended to handle these problems.
- 7.1. Polishing. One standard trick is to use the basic l1 filtering problem as a method to identify the kink points in the estimated trend. Once the kinks points {t1, . . . , tp} are identified, we use a standard least-squares method to fit the data over all piecewise-linear functions with the given kinks points:

$$& \minimize \quad \sum _ { k = 1 } ^ { p - 1 } \sum _ { t _ { k } \leq t \leq t _ { k + 1 } } \| y - \alpha _ { k } - \beta _ { k } t \| _ { 2 } ^ { 2 } \\ & \text {subject to } \quad \alpha _ { k } + \beta _ { k } t _ { k + 1 } = \alpha _ { k + 1 } + \beta _ { k + 1 } t _ { k + 1 } , \quad k = 1 , \dots , p - 2 ,$$

where the variables are the local trend parameters αk and βk. This technique is described (in another context) in, e.g., [12, sect. 6.5].

- 7.2. Iterative Weighted l1 Heuristic. The basic l1 trend filtering method is equivalent to

$$\min \min i t s _ { \substack { \minimize & \quad \| D x \| _ { 1 } \\ \text {subject to } & \| y - x \| _ { 2 } \leq s ,$$

with an appropriate choice of parameter s. In this formulation, we minimize ∥Dx1 (our measure of smoothness of the estimated trend) subject to a budget on residual norm. This problem can be considered a heuristic for the problem of finding the piecewise-linear trend with the smallest number of kinks, subject to a budget on residual norm:

$$\begin{array} { r l } { \minimize } & c a r d ( D x ) } \\ { s u b j e c t o } & \| y - x \| _ { 2 } \leq s , } \end{array}$$

where card(z) is the number of nonzero elements in a vector z. Solving this problem exactly is intractable; all known methods require an exhaustive combinatorial search over all—or at least very many—possible combinations of kink points.

The standard heuristic for solving this problem is to replace card(Dx) with ∥Dx‖1, which gives us our basic l1 trend filter, i.e., the solution to (18). This basic method can be improved by an iterative method that varies the individual weights on the second-order differences in xt. We start by solving (18). We then define a weight vector as

$$w _ { t } \coloneqq 1 / ( \epsilon + | ( D x ) _ { t } | ) , \ \ t = 1 , \dots , n - 2 ,$$

where € is a small positive constant. This assigns the largest weight, 1/e, when (Dx)t = 0; it assigns large weight when |(Dx)t| is small; and it assigns relatively small weight when |(Dx)t| is larger. We then recompute xt as the solution of problem

```
minimize       || diag(w) D x||_1
    subject to      || y - x||_2 \leq s.

```

We then update the weights as above and repeat.


<!-- p:14 -->


This iteration typically converges in 10 or fewer steps. It often gives a modest decrease in the number of kink points card(Dx), for the same residual, compared to the basic l1 trend estimation method. The idea behind this heuristic has been used in portfolio optimization with transaction costs [69], where an interpretation of the heuristic for cardinality minimization is given. The reader is referred to [18] for a more extensive discussion on the iterative heuristic.

7.3. Convex Constraints and Penalty Functions. We can add convex constraints on the estimated trend, or use a more general convex penalty function to measure the residual. In both cases, the resulting trend estimation problem is convex, and therefore tractable. We list a few examples here.

Perhaps the simplest constraints are lower and upper bounds on xt, or the first or second differences of xt, as in

$$| x _ { t } | \leq M , \ \ t = 1 , \dots , n , \quad | x _ { t + 1 } - x _ { t } | \leq S , \ \ t = 1 , \dots , n - 1 .$$

Here we impose a magnitude limit M, and a maximum slew rate (or slope) S, on the estimated trend. Another interesting convex constraint that can be imposed on xt is monotonicity, i.e.,

$$x _ { 1 } \leq x _ { 2 } \leq \cdots \leq x _ { n - 1 } \leq x _ { n } .$$

Mions  o  s  om s  s ( nce regression, which has been extensively studied in statistics [3, 82]. (Related work on l1-regularized isotonic regression, in an engineering context, includes [40, 41].)

We can also replace the square function used to penalize the residual term yt — xt with a more general convex function ψ. Thus, we compute our trend estimate xt as the minimizer of (the convex function)

$$\sum _ { t = 1 } ^ { n } \psi ( y _ { t } - x _ { t } ) + \lambda \| D x \| _ { 1 } .$$

For example, using ψ(u) = |u|, we assign a smaller penalty (compared to ψ(u) = (1/2)u2) to large residuals, but a larger penalty to small residuals. This results in a trend estimation method that is more robust to outliers than the basic l1 trend method since it allows large occasional errors in the residual. Another example is the Huber penalty function used in robust least squares, given by

$$\psi _ { h u b } ( u ) = \left \{ \begin{array} { l l } { u ^ { 2 } , } & { | u | \leq M , } \\ { M ( 2 | u | - M ) , } & { | u | > M , } \end{array}$$

where M ≥ 0 is a constant [53]. The use of an asymmetric linear penalty function of the form

$$\psi _ { \tau } ( u ) = \left \{ \begin{array} { l l } { \tau u , } & { u > 0 , } \\ { - ( 1 - \tau ) u } & { o t h e r w i s e , } \end{array}$$

where τ indicates the quantile of interest, is related to quantile smoothing splines. (The reader is referred to [59] for more on the use of this penalty function in quantile regression and [60] for more on quantile smoothing splines.)

In all of these extensions, the resulting convex problem can be solved with a computational effort that is O(n), since the system of equations that must be solved at each step of an interior-point method is banded.


<!-- p:15 -->


7.4. Multiple Components. We can easily extend basic l1 trend filtering to analyze time series data that involve other components, e.g., occasional spikes (outliers), level shifts, seasonal components, cyclic (sinusoidal) components, or other regression components. The problem of decomposing given time series data into multiple components has been a topic of extensive research; see, e.g., [11, 29, 45, 46] and the references therein. Compared with standard decomposition methods, the extensions described here are well suited to the case when the underlying trend, once the other components have been subtracted out, is piecewise linear.

Spikes. Suppose the time series data y has occasional spikes or outliers u in addition to trend and irregular components. Our prior information on the component u is that it is sparse. We can extract the underlying trend and the spike signal, by adding one more regularization term to (5), and minimizing the modified objective

$$( 1 / 2 ) \| y - x - u \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 1 } + \rho \| u \| _ { 1 } ,$$

where the variables are x (the trend component) and u (the spike component). Here the parameter λ ≥ 0 is used to control the smoothness (or number of slope changes) of the estimated trend, and ρ ≥ 0 is used to control the number of spikes.

Level Shifts. Suppose the time series data y has occasional abrupt level shifts. Level shifts can be modeled as a piecewise constant component w. To extract the level shift component w as well as the trend x, we add the scaled total variation of w, ρ∑t=2 |wt − wt-1|, to the weighted sum (5) and minimize the modified objective

$$( 1 / 2 ) \| y - x - w \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 1 } + \rho \sum _ { t = 2 } ^ { n } | w _ { t } - w _ { t - 1 } | ,$$

over x ∈ Rn and w ∈ Rn. Here the parameter λ ≥ 0 is used to control the smoothness of the estimated trend x, and ρ ≥ 0 is used to control the frequency of level shifts in w.

Periodic Components. Suppose the time series data y has an additive deterministic periodic component s with known period p:

$$s _ { t + p } = s _ { t } , \ \ t = 1 , \dots , n - p .$$

The periodic component s is called "seasonal" when it models seasonal fluctuations; removing effects of the seasonal component from y in order to better estimate the trend component is called seasonal adjustment. (The corresponding decomposition problem Hia              s )

Seasonal adjustment is readily incorporated in l1 trend filtering: We simply solve the (convex) problem

$$\min i m i z e \quad ( 1 / 2 ) \| y - x - s \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 1 } \\ \text {subject to } \quad s _ { t + p } = s _ { t } , \quad t = 1 , \dots , n - p , \\ \sum _ { k = 1 } ^ { p } s _ { k } = 0 , \\$$

where the variables are x (the estimated trend) and s (the estimated seasonal compo ns nt ont t tant dt nt t tsnt tt .n zero over the period; without this constraint, the decomposition is not unique [34, sect. 6.2.8]. To smooth the periodic component, we can add a penalty term to the objective, or impose a constraint on the variation of s. As a generalization of this formulation, the problem of jointly estimating multiple periodic components (with different periods) as well as a trend can be cast as a convex problem.


<!-- p:16 -->


When the periodic component is sinusoidal, i.e., st = a sin ωt + b cos ωt, where ω is the known frequency, the decomposition problem simplifies to

$$\minimize \ ( 1 / 2 ) \sum _ { t = 1 } ^ { n } \| y _ { t } - x _ { t } - a \sin \omega t - b \cos \omega t \| _ { 2 } ^ { 2 } + \lambda \| D x \| _ { 1 } ,$$

where the variables are x ∈ Rn and a, b ∈ R. (H-P filtering has also been extended to estimate trend and cyclic components; see, e.g., [39, 47].)

Regression Components. Suppose that the time series data y has autoregressive (AR) components in addition to the trend x and the irregular component z:

$$y _ { t } = x _ { t } + a _ { 1 } y _ { t - 1 } + \cdots + a _ { r } y _ { t - r } + z _ { t } ,$$

where ai are model coefficients. (This model is a special type of multiple structural change time series model [100].) We can estimate the trend component and the AR model coefficients by solving the l1-regularized least squares problem

$$\minimize \ ( 1 / 2 ) \sum _ { i = 1 } ^ { n } ( y _ { t } - x _ { t } - a _ { 1 } y _ { t - 1 } - \cdots - a _ { r } y _ { t - r } ) ^ { 2 } + \lambda \| D x \| _ { 1 } ,$$

where the variables are xt ∈ Rn and a = (a1, ... , ar) ∈ R". (We assume that y1−r, . . , y0 are given.)

7.5. Vector Time Series. The basic l1 trend estimation method can be generalized to handle vector time series data. Suppose that yt ∈ Rk for t = 1, . . . , n. We can find our trend estimate xt ∈ Rk, t = 1, . . . , k, as the minimizer of (the convex function)

$$\sum _ { t = 1 } ^ { n } \| y _ { t } - x _ { t } \| _ { 2 } ^ { 2 } + \lambda \sum _ { t = 2 } ^ { n - 1 } \| x _ { t - 1 } - 2 x _ { t } + x _ { t + 1 } \| _ { 2 } ,$$

where λ ≥ 0 is the usual parameter. Here we use the sum of the l2 norms of the second differences as our measure of smoothness. (If we use the sum of l1 norms, then the individual components of xt can be estimated separately.) Compared to estimating trends separately in each time series, this formulation couples together changes in the slopes of individual entries at the same time index, so the trend component found tends to show simultaneous trend changes, in all components of xt, at common kink points. (The idea behind this penalty is used in the group Lasso [105] and in compressed sensing involving complex quantities and related to total variation in two- or higherdimensional data [17, 84].) The common kink points can be interpreted as common abrupt changes or events in the underlying dynamics of the vector time series.

7.6. Spatial Trend Estimation. Suppose we are given two-dimensional data yi,j , on a uniform grid (i, j) ∈ {1, . . . , m} × {1, . . . , n}, assumed to consist of a relatively slowly varying spatial trend component xi,j and a more rapidly varying component vi,j. The values of the trend component at node (i, j) and its 4 horizontally or vertically adjacent nodes are on a linear surface if both the horizontal and vertical second-order differences, xi−1,j − 2xij + xi+1j and xi,j−1 − 2xi,j + xi,j+1, are zero.


<!-- p:17 -->


As in the vector time series case, we minimize a weighted sum of the fitting error Σi=1 Σ =1 ji, i,j||2 ad thd pennalty

$$\sum _ { i = 2 } ^ { m - 1 } \sum _ { j = 2 } ^ { n - 1 } [ ( x _ { i - 1 , j } - 2 x _ { i , j } + x _ { i + 1 , j } ) ^ { 2 } + ( x _ { i , j - 1 } - 2 x _ { i , j } + x _ { i , j - 1 } ) ^ { 2 } ] ^ { 1 / 2 }$$

on slope changes in the horizontal and vertical directions. It is possible to use more sophisticated measures of the smoothness, for example, determined by a 9-point approximation that includes 4 diagonally adjacent nodes.

The resulting trend estimates tend to be piecewise linear; i.e., there are regions over which xt is affine. The boundaries between regions can be interpreted as curves along which the underlying gradient changes rapidly.

7.7. Continuous-Time Trend Filtering. Suppose that we have noisy measurements (ti, yi), i = 1, . . . , n, of a slowly varying continuous function at irregularly spaced ti (in increasing order). In this section we consider the problem of estimating the underlying continuous trend from the finite number of data points. This problem involves an infinite-dimensional set of functions, unlike the trend filtering problems considered above. (Related segmented regression problems have been studied in [38, 54, 63].)

We first consider a penalized least squares problem of the form

$$\min \min i { 2 ( 1 / 2 ) \sum _ { i = 1 } ^ { n } ( y _ { i } - x ( t _ { i } ) ) ^ { 2 } + \lambda } \int _ { t _ { 1 } } ^ { t _ { n } } ( x ( t ) ) ^ { 2 } \, d t$$

over the space of all functions on the interval [t1, tn] with square integrable second derivative. Here, λ is a parameter used to control the smoothness of the solution. The solution is a cubic spline with knots at ti, i.e., a piecewise polynomial of degree 3 on R with continuous first and second derivatives; see, e.g., [33, 50, 98]. H-P filtering can be viewed as an approximate discretization of this continuous function estimation problem, when ti are regularly spaced: ti = t1 + (i − 1)h for some h &gt; 0. If the second derivative of x at ti is approximated as

$$x ( t _ { i } ) \approx \frac { x ( t _ { i - 1 } ) - 2 x ( t _ { i } ) + x ( t _ { i + 1 } ) } { h } , \ \ i = 2 , \dots , n - 1 ,$$

then the objective of the continuous-time problem (19) reduces to the weighted sum objective (1) of H-P filtering with regularization parameter λ/h.

We next turn to the continuous time l1 trend filtering problem

$$( 2 0 ) \quad \minimize _ { i = 1 } \ ( 1 / 2 ) \sum _ { i = 1 } ^ { n } ( y _ { i } - x ( t _ { i } ) ) ^ { 2 } + \lambda \int _ { t _ { 1 } } ^ { t _ { n } } | x ( t ) | \, d t$$

over

$$\chi = \left \{ x \colon [ t _ { 1 } , t _ { n } ] \to \mathbf R \, \Big | \, x ( t ) = \theta _ { 0 } + \theta _ { 1 } t + \int _ { t _ { 1 } } ^ { t _ { n } } \max ( t - s , 0 ) \, d \mu ( s ) , \, \theta _ { 0 } , \theta _ { 1 } \in \mathbf R , \, V ( \mu ) < \infty \right \} ,$$

where V(μ) is the total variation of the measure μ on [t1, tn]. (This function space includes piecewise linear continuous functions with a finite number of knots; see [78].) The difference from (19) is that in the integral term the second derivative is penalized using the absolute value function.


<!-- p:18 -->


A standard result in interpolation theory [78] is that the solution of the interpolation problem

$$\int ^ { t _ { n } }$$

$$\minimize & \quad \int _ { t _ { 1 } } ^ { t _ { n } } | x ( t ) | \, d t \\ \text {subject to } & \quad x ( t _ { i } ) = y _ { i } , \quad i = 1 , \dots , n ,$$

over X is continuous piecewise linear with knots at the points ti. From this, we can see that the solution to the continuous time l1 trend filtering problem (20) is also piecewise continuous linear with knots at the points ti; i.e., it is a linear spline. The second derivative of a piecewise linear function x with knots at the points ti is given by

$$x ( t ) = \sum _ { i = 2 } ^ { n - 1 } \left ( \frac { x ( t _ { i + 1 } ) - x ( t _ { i } ) } { t _ { i + 1 } - t _ { i } } - \frac { x ( t _ { i } ) - x ( t _ { i - 1 } ) } { t _ { i } - t _ { i - 1 } } \right ) \delta ( t - t _ { i } ) ,$$

where δ is the Dirac delta function. (The coefficients are slope changes at the kink points.) The integral of the absolute value of the second derivative is

$$\int _ { t _ { 1 } } ^ { t _ { n } } | x ( t ) | \, d t = \sum _ { i = 2 } ^ { n - 1 } \left | \frac { x ( t _ { i + 1 } ) - x ( t _ { i } ) } { t _ { i + 1 } - t _ { i } } - \frac { x ( t _ { i } ) - x ( t _ { i - 1 } ) } { t _ { i } - t _ { i - 1 } } \right | .$$

Thus the continuous l1 filtering problem (20) is equivalent to the (finite-dimensional) convex problem

$$\minimize \ ( 1 / 2 ) \sum _ { i = 1 } ^ { n } ( y _ { i } - x _ { i } ) ^ { 2 } + \lambda \sum _ { i = 2 } ^ { n - 1 } \left | \frac { x _ { i + 1 } - x _ { i } } { t _ { i + 1 } - t _ { i } } - \frac { x _ { i } - x _ { i - 1 } } { t _ { i } - t _ { i - 1 } } \right |$$

with variables (x1, . . . , xn) ∈ Rn. From the optimal points (ti, xi), we can easily recover the solution to the original continuous trend filtering problem: the piecewiselinear function that connects (ti, xi),

$$x ^ { * } ( t ) = \frac { t - t _ { i } } { t _ { i + 1 } - t _ { i } } x _ { i + 1 } ^ { * } + \frac { t _ { i + 1 } - t } { t _ { i + 1 } - t _ { i } } x _ { i } ^ { * } , \quad t \in ( t _ { i } , t _ { i + 1 } ) ,$$

is the optimal continuous trend that minimizes (20). When ti are regularly spaced, this problem reduces to the basic l1 trend filtering problem considered in section 3. For the same reason, we can solve (21) (and hence (20)) in O(n) arithmetic operations.

7.8. Segmented Polynomial Regression. Thus far our focus has been on fitting a piecewise-linear function to the given data. We can extend the idea to fitting a piecewise polynomial of degree k-1 to the data. Using a weighted l1 norm of the kth-order difference of x as a penalty term, the extension can be formulated as

$$\minimize \ ( 1 / 2 ) \sum _ { i = 1 } ^ { n } ( y _ { i } - x _ { i } ) ^ { 2 } + \lambda \| D ^ { ( k , n ) } x \| _ { 1 } .$$

Here D(k,n) ∈ R(n−k)×n is the kth-order difference matrix on Rn, defined recursively as

$$D ^ { ( k , n ) } = D ^ { ( 1 , n - k + 1 ) } D ^ { ( k - 1 , n ) } , \ \ k = 2 , 3 , \dots ,$$


<!-- p:19 -->


where D(1,p) ∈ R(p−1)×p is the first-order difference matrix on Rp,

1 -1


D(1,p) =

·..

1 -1


nh      s    os o st t tnt s tt sns t ns '(  st tt tt ton et solved at each step of an interior-point method is banded with bandwidth linear in k.

The resulting trend estimate xt tends to be piecewise polynomial of order k −1, i.e., there are regions over which xt is polynomial of order k − 1. The case of k = 1 corresponds to piecewise constant fitting and the case of k = 2 corresponds to piecewise-linear fitting.

Acknowledgments. The authors thank Trevor Hastie, Johan Lim, Michael Lustig, Almir Mutapcic, and Robert Tibshirani for helpful comments and suggestions.
