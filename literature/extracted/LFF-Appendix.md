---
id: "LFF-Appendix"
source_pdf: "../pdf/LFF-Appendix.pdf"
source_filename: "LFF-Appendix.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 98.0
visual_assets: "disabled"
---

<!-- p:1 -->

## Appendix to "Low Frequency Filtering and Real Business Cycles,

Journal of Economic Dynamics and Control, 1993, 17: 207-231.

Robert G. King and Sergio Rebelo where,


<!-- p:2 -->


$$F ( B ) & = \lambda \left [ B ^ { - 2 } - 4 B ^ { - 1 } + \left ( 6 + \frac { 1 } { \lambda } \right ) - 4 B + B ^ { 2 } \right ] \\ & = \lambda \left [ ( 1 - B ) ^ { 2 } \left ( 1 - B ^ { - 1 } \right ) ^ { 2 } + \frac { 1 } { \lambda } \right ] .$$

A.1. Zeros of F Polynomial

We develop properties of the polynomial F(z), especially the location of its zeros, establishing the claims made in the main text.

(a) Reciprocal Character of Roots - since the polynomial F(z) is symmetric if z* is a root then 1/z* is also a root. To see this, it can be shown that F(z) = λ [(1 − z) (1 − 1)2 + −] for arbitrary z. Thus, if z* implies F(z*) = λ[(1 − z*)2 (1 − 1)2 + 1] = 0 then F(1) = λ[(1 − 1)2(1 − z*)2 + μ] = F(z*) = 0.

- (b) Complex Character of Roots - For any real number z, F(z) &gt; 0. Thus, the roots must be complex. Further, it follows that z* and are complex 2* conjugates.

### A.2. Inverting F(B) and Related Matters

The previous results imply that we can express F(B) as:

$$F ( B ) = \left ( \frac { \lambda } { \theta _ { 1 } \theta _ { 2 } } \right ) \left ( 1 - \theta _ { 1 } B \right ) \left ( 1 - \theta _ { 2 } B \right ) \left ( 1 - \theta _ { 1 } B ^ { - 1 } \right ) \left ( 1 - \theta _ { 2 } B ^ { - 1 } \right ) ,$$

where |θi| &lt; 1, for i = 1, 2.

Thus to determine a useful form for [F(B)]−1 = G(B), it is necessary to decompose:

$$\underline { 1 } \cdot \underline { 1 } \cdot \underline { 1 } \cdot \underline { 1 } \cdot \underline { 1 }$$

$$\frac { 1 } { 1 - \theta _ { 1 } z } \frac { 1 } { 1 - \theta _ { 2 } z } \frac { 1 } { 1 - \theta _ { 1 } z ^ { - 1 } } \frac { 1 } { 1 - \theta _ { 2 } z ^ { - 1 } } \\ \\ A _ { 0 } + \frac { A _ { 1 } } { 1 - \theta _ { 1 } z } + \frac { A _ { 2 } } { 1 - \theta _ { 2 } z } + \frac { A _ { 3 } } { 1 - \theta _ { 1 } z ^ { - 1 } } + \frac { A _ { 4 } } { 1 - \theta _ { 2 } z ^ { - 1 } } .$$

into

$$A _ { 0 } + \frac { A _ { 1 } } { 1 - \theta _ { 1 } z } + \frac { A _ { 2 } } { 1 - \theta _ { 2 } z } + \frac { A _ { 3 } } { 1 - \theta _ { 1 } z ^ { - 1 } } + \frac { A _ { 4 } } { 1 - \theta _ { 2 } z ^ { - 1 } } .$$

To determine A0,A1, A2, A3, and A4 we require that:

$$\begin{array} { r l r } { 1 } & { = } & { A _ { 0 } \left ( 1 - \theta _ { 1 } z \right ) \left ( 1 - \theta _ { 2 } z \right ) \left ( 1 - \theta _ { 1 } z ^ { - 1 } \right ) \left ( 1 - \theta _ { 2 } z ^ { - 1 } \right ) } \\ & { + A _ { 1 } \left ( 1 - \theta _ { 2 } z \right ) \left ( 1 - \theta _ { 1 } z ^ { - 1 } \right ) \left ( 1 - \theta _ { 2 } z ^ { - 1 } \right ) + A _ { 2 } \left ( 1 - \theta _ { 1 } z \right ) \left ( 1 - \theta _ { 1 } z ^ { - 1 } \right ) \left ( 1 - \theta _ { 2 } z ^ { - 1 } \right ) } \\ & { + A _ { 3 } \left ( 1 - \theta _ { 1 } z \right ) \left ( 1 - \theta _ { 2 } z \right ) \left ( 1 - \theta _ { 2 } z ^ { - 1 } \right ) + A _ { 4 } \left ( 1 - \theta _ { 1 } z \right ) \left ( 1 - \theta _ { 2 } z \right ) \left ( 1 - \theta _ { 1 } z ^ { - 1 } \right ) . } \end{array}$$

## Appendix A

Analysis of the HP Filter in Time Domain

The starting point for our analysis is the (first order) condition/requirement that:

$$y _ { t } = F ( B ) y _ { t } ^ { g }$$


<!-- p:3 -->


Evaluating this expression at z = 1 yields:

$$1 1 1 1 A1 A2 A3 A4 1 − θ1 1 − θ2 1 − θ1 1 − θ2 = A0 + 1 − θ1 十 1 − θ2 十 1 − θ1 十 1 − θ2$$

Evaluating this expression at z = 1 yields: θ1

$$A _ { 1 } = \left [ \left ( 1 - \frac { \theta _ { 2 } } { \theta _ { 1 } } \right ) \left ( 1 - \theta _ { 1 } ^ { 2 } \right ) \left ( 1 - \theta _ { 2 } \theta _ { 1 } \right ) \right ] ^ { - 1 } , \\$$

and evaluating at the other roots yields:

$$A _ { 2 } & = \left [ \left ( 1 - \frac { \theta _ { 1 } } { \theta _ { 2 } } \right ) ( 1 - \theta _ { 1 } \theta _ { 2 } ) \left ( 1 - \theta _ { 2 } ^ { 2 } \right ) \right ] ^ { - 1 } , \\ A _ { 3 } & = \left [ \left ( 1 - \theta _ { 1 } ^ { 2 } \right ) ( 1 - \theta _ { 1 } \theta _ { 2 } ) \left ( 1 - \frac { \theta _ { 2 } } { \theta _ { 1 } } \right ) \right ] ^ { - 1 } , \\$$

$$A _ { 4 } = \left [ ( 1 - \theta _ { 1 } \theta _ { 2 } ) \left ( 1 - \theta _ { 2 } ^ { 2 } \right ) \left ( 1 - \frac { \theta _ { 1 } } { \theta _ { 2 } } \right ) \right ] ^ { - 1 } .$$

Some useful properties of these expressions are as follows. First, A1 = A3 and A2 = A4. Second, A1 and A2 are complex conjugates, as is most readily evident if we move to the (polar form) representation θ1 = r exp (im) and θ2 = r exp (—im) . Then, when we substitute these expressions for θ1 and θ2 into the preceding expressions for A1 and A2, we find that:

$$A _ { 1 } = \left [ ( 1 - e x p \left ( - 2 i m \right ) ) \left ( 1 - r ^ { 2 } e x p \left ( 2 i m \right ) \right ) \left ( 1 - r ^ { 2 } \right ) \right ] ^ { - 1 }$$

$$A _ { 2 } = \left [ ( 1 - e x p \left ( 2 i m \right ) ) \left ( 1 - r ^ { 2 } e x p \left ( - 2 i m \right ) \right ) \left ( 1 - r ^ { 2 } \right ) \right ] ^ { - 1 } ,$$

so that the conjugate status of these coefficients becomes clear. Hence, combining the results of the forgoing, we can express the growth filter as:

$$G ( B ) = [ F ( B ) ] ^ { - 1 }$$

$$= & \left [ \frac { \theta _ { 1 } \theta _ { 2 } } { \lambda } \right ] \left \{ A _ { 0 } + \left [ \frac { A _ { 1 } } { 1 - \theta _ { 1 } B } + \frac { A _ { 2 } } { 1 - \theta _ { 2 } B } \right ] + \left [ \frac { A _ { 1 } } { 1 - \theta _ { 1 } B ^ { - 1 } } + \frac { A _ { 2 } } { 1 - \theta _ { 2 } B ^ { - 1 } } \right ] \right \} .$$

### A.3. Coefficients in the Growth Filter

To establish that the coefficients in the growth filter - which depend on A1θ1 + A2θ2 for j ≥ 0 - are real, it is again convenient to adopt the polar form representation:

$$\theta _ { 1 } = r \ e x p \ ( i m )$$


<!-- p:4 -->


Then it follows that:

$$\begin{array} { r l r } { \left [ A _ { 1 } \theta _ { 1 } ^ { j } + A _ { 2 } \theta _ { 2 } ^ { j } \right ] } & { = } & { R r ^ { j } \ e x p \ ( i \left ( M + j m \right ) ) + R r ^ { j } \ e x p \ ( - i \left ( M + j m \right ) ) } \\ & { = } & { 2 R r ^ { j } \, \cos \left ( M + j m \right ) . } \end{array}$$

∞ Thus, we can write G(B) = ∑ gjBj as: j=-∞

$$0 + 2 R \sum _ { j = 0 } ^ { \infty } r ^ { j } \cos \left ( M + j m \right ) B ^ { j } + 2 R \sum _ { j = 0 } ^ { \infty } r ^ { j } \cos \left [ 0 + 0 \right ]$$

which indicates that the roots are real. Further, using cos (jm + M) = [cos (mj) cos (M) − sin (mj) sin (M)] it is direct to establish the form of the filter provided by Hodrick and Prescott (1980) and Singleton (1988). For this purpose, we note that A0 turns out to be -2R cos(M). Then, the previous expression for G(B) may be written as:

$$G ( B ) = \sum _ { j = - \infty } ^ { \infty } g _ { j } B ^ { j }$$

where

$$\begin{array} { r c l } g _ { j } & = & r ^ { j } a _ { 1 } \cos ( b j ) + a _ { 2 } s i n ( b j ) & f o r \ j \geq 0 \\ g _ { j } & = & g _ { - j } & f o r \ j \leq 0 \end{array}$$

with the constants a1 = [] 2R cos(M), a2 = 2R sin(M), b = |m| .

$$\theta _ { 2 } = r \ e x p \ ( - i m )$$

$$A _ { 1 } = R \ e x p \ ( i M )$$

$$A _ { 2 } = R \ e x p \ ( - i M ) \, .$$


<!-- p:5 -->


## Appendix B

Inverse Optimal Linear Filtering

Taking as given a specific filter, the Hodrick and Prescott (1980) filter in our context, one can ask what the implicit model for the underlying series must be for this filter to be optimal, in the sense of minimizing the mean square error as in Wiener (1949) and Whittle (1963). In order to be possible for the HP filter to be optimal we start with a statistical representation of the underlying time series which is linear and in which growth and cycles are separate phenomena.

Suppose that we view the growth and cyclical components as being generated by ARMA models:

$$\begin{array} { r c l } A ^ { g } ( B ) \ y _ { t } ^ { g } & = & M ^ { g } ( B ) \ \epsilon _ { t } ^ { g } \\ A ^ { c } ( B ) \ y _ { t } ^ { c } & = & M ^ { c } ( B ) \ \epsilon _ { t } ^ { c } \end{array}$$

where ea and ∈c are white noise processes whose variances are s2(εc) and s2(ε9). By assumption, the roots of the autoregressive polynomials lie outside the unit circle (stationarity) and the roots of the moving average polynomial lie outside the unit circle (invertibility). The innovations ea and ∈f are serially uncorrelated and, for simplicity, we assume that E[e¿ €] = 0. Further, for s2(∈c) convenience, we define the ratio of variances ψ = . (6∂)zs+(s)zs

Whittle (1963, chapter V) shows that the optimal (two sided) signal extraction filter for the cyclical component is:

$$C ^ { * } ( B ) = \frac { \Gamma _ { c c } ( B ) } { \Gamma _ { c c } ( B ) + \Gamma _ { g g } ( B ) }$$

where Γcc(B) is the autocovariance generating function of the cyclical component and Γgg(B) is the autocovariance generating function of the growth component. From the ARMA structure it follows directly that:

$$\begin{array} { r l } { \Gamma _ { c c } ( z ) } & { = } & { \frac { M ^ { c } ( z ) M ^ { c } ( z ^ { - 1 } ) } { A ^ { c } ( z ) A ^ { c } ( z ^ { - 1 } ) } s ^ { 2 } ( \epsilon _ { t } ^ { c } ) } \\ { \Gamma _ { g g } ( z ) } & { = } & { \frac { M ^ { g } ( z ) M ^ { g } ( z ^ { - 1 } ) } { A ^ { g } ( z ) A ^ { g } ( z ^ { - 1 } ) } s ^ { 2 } ( \epsilon _ { t } ^ { g } ) . } \end{array}$$

Hence, it follows that the optimal filter may be expressed as:

$$C ^ { A } ( B ) = \frac { \psi A ^ { g } ( B ) A ^ { g } ( B ^ { - 1 } ) } { \psi A ^ { g } ( B ) A ^ { g } ( B ^ { - 1 } ) + ( 1 - \psi ) Q ( B ) } \\ \text {where } Q ( B ) = \frac { [ A ^ { c } ( B ) A ^ { c } ( B ^ { - 1 } ) ] [ M ^ { g } ( B ) M ^ { g } ( B ^ { - 1 } ) ] } { M ^ { g } ( B ) M ^ { c } ( B ^ { - 1 } ) } . \\ \text {Whitel's} o n o l i v i o n ( 1 0 6 3 ) \text { is lifted to at optionuary } A \cap [ A \cap M ] \cap [ A \cap M ] \text { .}$$

Whittle's analysis (1963) is limited to stationary ARMA processes. However, recent work extends these formulas to cases with unit roots (Watson (1986) provides a brief summary of Bell's (1984) work on these cases).


<!-- p:6 -->


#### Matching the HP Cyclical Filter

The HP cyclical filter may be written as:

$$C ( B ) = [ F ( B ) - 1 ] \left [ F ( B ) ^ { - 1 } \right ] = \frac { \lambda \left [ 1 - B \right ] ^ { 2 } \left [ 1 - B ^ { - 1 } \right ] ^ { 2 } } { 1 + \lambda \left [ 1 - B \right ] ^ { 2 } \left [ 1 - B ^ { - 1 } \right ] ^ { 2 } }$$

The problem is to find AR and MA polynomials (Aa(B), Ac(B), M9(B), and Mc(B)) such that C(B) and C*(B) coincide.

One example of such an inverse optimal filtering rule is discussed by Hodrick and Prescott (1980, p. 5) and involves assuming that:

$$A ^ { g } ( B ) \ = \ ( 1 - B ) ^ { 2 }$$

$$A ^ { c } ( B ) \ = \ M ^ { g } ( B ) = M ^ { c } ( B ) = 1 .$$

That is, under this specification, the change in the growth rate is a white noise as is the cyclical component. Further, the parameter λ corresponds to ψ which is equal to the ratio of variances λ = s2(∈c) = (1/I) 1) s(∈c) Hodrick (h-1) s2(€9) s(e9) and Prescott (1980) use a "prior view that a five percent cyclical component is moderately large as is a one-eighth of one percent change in the rate of growth in a quarter. This led us to select λ(1/2) 5 or λ = 1600 as a value for the (1/8) smoothing parameter."

Pursuing this line further, suppose that we require that A9(B) = (1 − B)2 so as to accommodate nonstationarity in the growth rate. Then, it follows that C(B) = C*(B) requires that:

$$\frac { 1 } { \lambda } = \frac { 1 - \psi } { \psi } Q ( B ) .$$

Thus, the optimality of the HP filter requires - apart from the constant terms - restrictions across the Ac(B), Mc(B), and Ma(B) polynomials. In particular it requires that:

$$M ^ { c } ( B ) = \left [ \frac { \lambda ( 1 - \psi ) } { \psi } \right ] ^ { ( 1 / 2 ) } A ^ { c } ( B ) M ^ { g } ( B ) .$$

In our view, these sorts of restrictions are unlikely to arise directly from the structure of dynamic economic models since in these models growth and cycles do not tend to arise as separate phenomena.
