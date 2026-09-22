---
id: "13_New_Method_of_Graduation"
source_pdf: "../pdf/13_New_Method_of_Graduation.pdf"
source_filename: "13_New_Method_of_Graduation.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "hybrid"
extraction_quality: "good"
extraction_score: 88.0
visual_assets: "disabled"
---

<!-- p:1 -->

## On a New Method of Graduation.

By Professor E. T. WHITTAKER, F.R.S

(Read 14th Nov. 1919. Received, in amended form, 8th Aug. 1923).

§1. Introductory.

Suppose that as a result of obseryation or experience of some kind we have obtained a set of values of a variable u corresponding to equidistant values of its argument; let these be denoted by u1, u2, ... un If they have been derived from observations of some natural phenomenon, they will be affected by errors of observation ; if they are statistical data derived from the examination of a comparatively small field, they will be affected by irregularities arising from the accidental peculiarities of the field ; that is to say, if we examine another field and derive a set of values of u from it, the sets of values of u derived from the two fields will not in general agree with each other In any case, if we form a table of the differences ∆u1 = ug − u1, ∆u2 = us − u2, ... , ∆2u1= Δuz- ∆u1, etc., it will generally be found that these differences are so irregular that the difference-table cannot be used for the purposes to which a difference-table is usually put, viz., finding interpolated values of u, or differential coefficients of u with respect to its argument, or definite integrals involving u; before we can use the difference-tables we must perform a process of "smoothing," that is to say, we must find another sequence u1', u2', u3', ... , u,', whose terms differ as little as possible from the terms of the sequence u1, ug, ... u, but which has regular differences. This smoothing process, leading to the formation of ui', u', ... u,', is called the graduation or adjustment of the observations.

Workers in experimental science generally deal with the problem by plotting the numbers u1, "g, ... u, against the corresponding value of the argument, and drawing a freehand curve as nearly as possible through them. This somewhat arbitrary method is insufficient for the needs of Actuarial Science, and a large number of "graduation formulae" are to be found in the journals of the Actuarial Societies.


<!-- p:2 -->


The standpoint of the present paper is, that the problem belongs essentially to the mathematical theory of Probability ; we have the given observations, and they would constitute the "most probable" values of u for the corresponding values of the argument, were it not that we have à priori grounds for believing that the true values of u form a smooth series, the irregularities being due to accidental causes which it is desirable to eliminate, The problem is to combine all the materials of judgment—the observed values and the à priori considerations—in order to obtain the resulting "most probable" values of u.

## §2. The basis of the method in the theory of Probability.

Let us then suppose tbat we are concerned with a number uz which depends on an argument x, and suppose that we have n data u1, u2, ... u, which are affected with uncertainties or irregularities due, e.g., to accidental errors of observation; so that when ux is plotted as a function of x, the n points so obtained do not lie on a smooth curve, although there is a strong antecedent probability that if the observations had been more accurate the curve would have been smooth. We may make the somewhat vague word t m  s n  e t  rr, differences ∆aux are to be very small.

Now consider the following hypothesis; that the true value which should have been obtained by the observation for u, lies between u1' and u1'+σ where σ is a small constant number; that the true value which shouid have been obtained by the observation for ug lies between u2' and u2' + σ, etc., and finally, that the true value which should have been obtained by the observation for u lies between un' and un'+σ. This hypothesis we shall call "hypothesis H."

Before the observations have been made we have nothing to guide us as to the probability of this hypothesis H except the degree of smoothness of the sequence ui', u', ..., un', which may be measured by the smallness of the sum of the squares of the third differences *

$$\begin{array} { c } \i = ( u _ { 4 } ^ { \prime } - 3 u _ { 3 } ^ { \prime } + 3 u _ { 2 } ^ { \prime } - u _ { 1 } ) ^ { 2 } + ( u _ { 5 } ^ { \prime } - 3 u _ { 4 } ^ { \prime } + 3 u _ { 3 } ^ { \prime } - u _ { 2 } ^ { \prime } ) ^ { 2 } + \dots \\ - \dots \\ \end{array} + ( u _ { n } ^ { \prime } - 3 u _ { n - 1 } ^ { \prime } + 3 u _ { n - 2 } ^ { \prime } - u _ { n - 3 } ^ { \prime } ) ^ { 2 } .$$

* The theory may be extended to the case when the observations are not taken at equidistant values of the argument, by taking instead of S the sum of the squares of the third divided differences of the graduated values.


<!-- p:3 -->


We may therefore, by analogy with the normal law of frequency, e e p o e iie  t tt ns on where c and λ denote constants.

Next, let us consider the à priori probability that the measures obtained by the observations will be u1, u2, .. u, on the assumption that hypothesis H is true. Since the true value of the first observed quantity is, on this hypothesis, u1', the probability that a value between u1 and u+σ will actually be observed will (postulating the normal law of error) be

$$\frac { h _ { 1 } } { \sqrt { \pi } } \, e ^ { - h _ { 1 } ^ { 2 } ( u _ { 1 } - u _ { 1 } \prime ) ^ { 2 } } \, \sigma \, , \\$$

where h, is a constant which measures the precision with which this observation can be made.

Similarly, the probability that a value between u2 and u2+ σ will actually be obtained for the second observed measure is

$$\frac { h _ { 2 } } { \sqrt { \pi } } \, e ^ { - h \hat { \Xi } ( u , - u _ { i } , \theta ) ^ { 2 } } \sigma , \\$$

where h2 is the measure of precision of this observation.

Thus, on the assumption that hypothesis H is true, the à priori probability that the observed measure of the first observed quantity will be between u, and u, +σ, the observed measure of the second observed quantity will be between u2 and u2 + σ, etc., is

where F denotes the sum

$$F = h _ { 1 } ^ { 2 } \, \left ( u _ { 1 } - u _ { 1 } ^ { \prime } \right ) ^ { 2 } + h ^ { 2 } \left ( u _ { 2 } - u _ { 2 } ^ { \prime } \right ) ^ { 2 } + \dots + h _ { \Re } ^ { \Re } \, \left ( u _ { \Re } - u _ { \Re } ^ { \prime } \right ) ^ { 2 } .$$

The sums S and F enable us to express numerically the smoothness of the graduated values, and the fidelity of the graduated to the ungraduated values, respectively.

We must now make use of the fundamental theorem in the theory of Inductive Probability, which is as follows:—Suppose hha   n  n  e ed  an one of a certain number of hypotheses, of which one, and not more than one, must be true: Suppose, moreover, that the probability of the sth hypothesis, as based on information in our possession before the phenomenon is observed, is p while the probability of the

6 Vol. 41


<!-- p:4 -->


observed phenomenon on the assumption of the truth of the sth hypothesis is P. Then when the observation of the phenomenon

is taken into consideration, the probability of the sth hypothesis is

where the symbol Σ denotes summation over all the hypotheses.

It follows from this that whereas before the phenomenon was observed, the most probable hypothesis was that for which p. was greatest, the most probable hypothesis after the phenomenon has been observed is that for which the product P.p. is greatest. Applying this theorem to the case under consideration, we see that the most probable hypothesis is that for which

is a maximum, that is to say, the most probable set ui', uy', ... un'

values of the quantities is that which makes of

$$\lambda ^ { 2 } S + F$$

a minimum.

§ 3. The analytical formulation.

Writing down the ordinary conditions for a minimum, we

obtain the equations

We shall now make the simplifying assumption that the measure of precision is the same for all the data, so

$$h _ { 1 } = h _ { 2 } = \dots = h _ { \bullet } \cdot ^ { * }$$

* If this is not the case, we graduate some funotion of u, such as logu, instead of u, choosing this function so that its measure of precision has nearly the same value for all values of the argument.


<!-- p:5 -->


If we write hi = h = .. = eλ2 the equations may now be written

$$1 1 \ w c \ ( 1 1 0 c \ \lambda _ { 1 } = \mu _ { \varepsilon } = \dots \stackrel { 1 } { 2 } \ \lambda \ \varepsilon \ \Delta u ( \Delta u _ { 1 } ^ { \prime } \ \lambda _ { 1 } = 0 ) \ w c \ \ w f r i n e { 1 } \\ \varepsilon u _ { 1 } = \varepsilon u _ { 1 } ^ { ^ { \prime } } - \Delta u _ { 1 } ^ { ^ { \prime } } \\ \varepsilon u _ { 2 } = \varepsilon u _ { 2 } ^ { ^ { \prime } } + 3 \Delta ^ { \varepsilon } u _ { 1 } ^ { ^ { \prime } } - \Delta ^ { \varepsilon } u _ { 2 } ^ { ^ { \prime } } \\ \varepsilon u _ { 3 } = \varepsilon u _ { 3 } ^ { ^ { \prime } } - 3 \Delta ^ { * } u _ { 1 } ^ { ^ { \prime } } + 3 \Delta ^ { 3 } u _ { 2 } ^ { ^ { \prime } } - \Delta ^ { * } u _ { 3 } ^ { ^ { \prime } } \cdot \Delta ^ { * } u _ { 4 } ^ { ^ { \prime } } \ \Big / \\ \varepsilon u _ { 4 } = \varepsilon u _ { 4 } ^ { ^ { \prime } } + \Delta ^ { 3 } u _ { 1 } ^ { ^ { \prime } } - 3 \Delta ^ { 3 } u _ { 2 } ^ { ^ { \prime } } + 3 \Delta ^ { 3 } u _ { 3 } ^ { ^ { \prime } } - \Delta ^ { * } u _ { 4 } ^ { ^ { \prime } } \ \Big / \\ \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots \dots$$

Now all the equations, except the three first and the three last, are of the form

$$\epsilon u _ { x } = \epsilon u _ { x } ^ { ^ { \prime } } - \Delta ^ { 6 } u _ { x - 3 } ^ { ^ { \prime } } .$$

Moreover, if we introduce a quantity un' such that ∆3 u′ = 0, the third equation becomes

$$\epsilon u _ { 3 } = \epsilon u _ { 3 } ^ { \prime } - \Delta ^ { 6 } u _ { 0 } ^ { \prime } ,$$

which is of the same form ; and similarly the first two and last three equations can be brought to the same form by introducing new quantities u'−1, u'−2, u'n+1, u'n+2 , u'n+3, such that

$$\Delta ^ { s } u ^ { \prime } _ { - 1 } = 0 , \ \Delta ^ { s } u ^ { \prime } _ { - 2 } = 0 , \ \Delta ^ { 3 } u ^ { \prime } _ { n - 2 } = 0 , \ \Delta ^ { 3 } u ^ { \prime } _ { n - 1 } = 0 , \ \Delta ^ { s } u ^ { \prime } _ { n } = 0 .$$

Thus the graduated values ui' satisfy the linear difference-equation

$$\epsilon u _ { x } ^ { \prime } - \Delta ^ { \Delta } u _ { x - 3 } ^ { \prime } = \epsilon u _ { z } ,$$

being in fact the particular solution of this equation which satisfies the six terminal conditions

$$\Delta ^ { \mathfrak { u } ^ { \prime } _ { 0 } = 0 , \, \Delta ^ { \mathfrak { u } ^ { \prime } _ { - 1 } = 0 , \, \Delta ^ { \mathfrak { u } ^ { \prime } _ { - 2 } = 0 , \, \Delta ^ { \mathfrak { u } ^ { \prime } _ { n - 2 } = 0 , \, \Delta ^ { \mathfrak { u } ^ { \prime } _ { n - 1 } = 0 , \, \Delta ^ { \mathfrak { u } ^ { \prime } _ { n } = 0 \dots ( 3 ) }$$

whence we have at once

$$\Delta ^ { u ^ { \prime } _ { - 2 } } = 0 , \, \Delta ^ { + u ^ { \prime } _ { - 1 } } = 0 , \, \Delta ^ { s } u ^ { \prime } _ { - \frac { 2 } { 2 } } = 0 , \, \Delta ^ { + } u ^ { \prime } _ { n - 2 } = 0 , \, \Delta ^ { 4 } u ^ { \prime } _ { n - 1 } = 0 , \, \Delta ^ { s } u ^ { \prime } _ { n - 2 } = 0 \ \ ( 4 )$$

§ 4. The Theorems of Conservation.

From (2) we have by summation

$$\epsilon ( u _ { 1 } ^ { \prime } + u _ { 2 } ^ { \prime } + \dots + u _ { n } ^ { \prime } ) - \epsilon \left ( u _ { 1 } + u _ { 2 } + \dots + u _ { n } \right ) & = \Delta ^ { u _ { n } ^ { \prime } } - \Delta ^ { u _ { n } ^ { \prime } } + \dots + \Delta ^ { \circ } u _ { n - 1 } ^ { \prime } + \dots + \Delta ^ { \circ } u _ { n - 1 } ^ { \prime } \\ & = \Delta ^ { u _ { n - 1 } ^ { \prime } - \Delta ^ { u _ { n - 2 } ^ { \prime } } } \\ & = 0 \quad \text {by } ( 4 ) .$$

$$T h e r e \quad u _ { 1 } ^ { \prime } + u _ { 2 } ^ { \prime } + \dots + u _ { n } ^ { \prime } = u _ { 1 } + u _ { 2 } + \dots + u _ { n } \quad \dots$$


<!-- p:6 -->


$$M o r e o v e r , b y \left ( 2 \right )$$

$$\text {Moreover, by (2)} \\ \epsilon ( u _ { 1 } ^ { \prime } + 2 u _ { 2 } ^ { \prime } + 3 u _ { 3 } ^ { \prime } + \dots + n u _ { n } ^ { \prime } ) - \epsilon ( u _ { 1 } + 2 u _ { 2 } + \dots + n u _ { n } ) \\ = \Delta ^ { 6 } u _ { - 2 } ^ { \prime } + 2 \Delta ^ { 5 } u _ { - 1 } ^ { \prime } + \dots + n \Delta ^ { 6 } u _ { n - 3 } ^ { \prime } \\ = n \Delta ^ { 6 } u _ { n - 2 } ^ { \prime } - \Delta ^ { 4 } u _ { n - 2 } ^ { \prime } + \Delta ^ { 4 } u _ { - 2 } ^ { \prime } \\ = 0 \quad \text {by (4)} . \\ \text {Therefor} \\ u _ { 1 } ^ { \prime } + 2 u _ { 2 } ^ { \prime } + 3 u _ { 3 } ^ { \prime } + \dots + n u _ { n } ^ { \prime } = n _ { 1 } + 2 u _ { 2 } + 3 u _ { 3 } + \dots + n u _ { n } \dots \dots \dots ( 6 ) \\ \text {Next, by (2)} \\ \epsilon ( u _ { 1 } ^ { \prime } + 2 ^ { 2 } u _ { 2 } ^ { \prime } + 3 ^ { 2 } u _ { 2 } ^ { \prime } + \dots + n ^ { 2 } u _ { n } ) - \epsilon ( u _ { 1 } + 2 ^ { 2 } u _ { 2 } + 3 ^ { 2 } u _ { 3 } + \dots + n ^ { 2 } u _ { n } ) \\ = \Delta ^ { 6 } u _ { n - 2 } ^ { \prime } + 2 ^ { 2 } \Delta ^ { 6 } u _ { - 1 } ^ { \prime } + \dots + n ^ { 2 } \Delta ^ { 6 } u _ { n } ^ { \prime } u _ { - 3 } ^ { \prime } \\ = n ^ { 2 } \Delta ^ { 5 } u _ { n - 2 } ^ { \prime } - ( 2 n - 1 ) \Delta ^ { 4 } u _ { n - 2 } ^ { \prime } + 2 \Delta ^ { 3 } u _ { n - 2 } ^ { \prime } - \Delta ^ { 3 } u _ { - 2 } ^ { \prime } - \Delta ^ { 3 } u _ { - 1 } \\ = 0 \quad \text {by (3) and (4)} . \\ \text {Therefor} \\ u _ { 1 } ^ { \prime } + 2 ^ { 2 } u _ { 2 } ^ { \prime } + 3 ^ { 2 } u _ { 3 } ^ { \prime } + \dots + n ^ { 2 } u _ { n } ^ { \prime } = u _ { 1 } + 2 ^ { 2 } u _ { 2 } + 3 ^ { 2 } u _ { 3 } + \dots + n ^ { 2 } u _ { n } \dots \dots ( 7 )$$

Therefore

$$u _ { 1 } ^ { \prime } + 2 ^ { 2 } u _ { 2 } ^ { \prime } + 3 ^ { 2 } u _ { 3 } ^ { \prime } + \dots + n ^ { 2 } u _ { 2 } ^ { \prime } = u _ { 1 } + 2 ^ { 2 } u _ { 2 } + 3 ^ { 2 } u _ { 3 } + \dots + n ^ { 2 } u _ { n }$$

Equations (5), (6), (7) show that the moments of orders 0, 1, 2 are the same for the graduated data as for the original data. This may be called the Theorem of Conservation of Moments. We may erp t t   t  es   ste data and the graph which represents the graduated data have the same area, the same x-coordinate of the centre of gravity, and the same moment of inertia about any line parallel to the axis of u.

Thus by this method we secure that the total of the u's and their first and second moments shall be the same in the graduated table as in the actual statistics on which it is based.

## § 5. The numerical process of graduation.

The parameter ε is at our disposal, and measures the importance which we attach to keeping close to the original data, as weighed against our desire to attain perfect smoothness in the graduated curve. If ε were taken absolutely zero we should obtain a perfectly smooth graduated curve which would have the same moments of orders 0, 1 and 2 as the ungraduated curve, but in other respects might not fit the observed data closely. In practice therefore we do not take e to be absolutely zero, but it may usually be taken to be a small number, so that it is convenient to expand the solution in ascending powers of € and retain only the part which is independent of ε together with the part which involves the first power of €: the parts involving higher powers of ε may be neglected.


<!-- p:7 -->


Suppose then that the terms in the graduated value ur' are arranged according to the powers of ∈ which they involve, thus

$$u _ { x } ^ { \, ^ { \prime } } = u _ { x , \, 0 } ^ { \prime } + \epsilon u _ { x , \, 1 } ^ { \prime } + \epsilon ^ { 2 } u _ { x , \, 2 } ^ { \prime } + \dots \quad .$$

Substituting in (2) and equating the coefficients of €, we have

$$\epsilon \, u _ { \varepsilon , \, 0 } ^ { \prime } - \Delta ^ { 6 } u _ { \varepsilon = 3 , \, 1 } ^ { \prime } = \epsilon \, u _ { \varepsilon }$$

which is a linear difference-equation to determine u'x,1, if u'x,o can first be found.

Now u'x,o can be found without difficulty in the following way : From equation (1) it follows at once that, when ε is zero, the third differences of the graduated values are all zero: so u'x,o must be a polynomial of degree two in x, say,

$$u _ { z , \, 0 } ^ { \prime } = a + b x + c x ^ { 2 } \ \dots \ \dots \ \dots \ \dots \ \ ( 1 0 )$$

where a, b, c, are independent of x. Substituting in equations (5), (6), (7), they become

$$\ n a + \{ n ( n + 1 ) \, b + \frac { 1 } { 6 } \, n ( n + 1 ) \, ( 2 n + 1 ) \, c & = M _ { 0 } \\ \S n ( n + 1 ) \, a + \frac { 1 } { 6 } \, n ( n + 1 ) \, ( 2 n + 1 ) \, b + \frac { 1 } { 6 } \, n ^ { 2 } ( n + 1 ) ^ { 2 } c & = M _ { 1 } \\ \frac { 1 } { 8 } \, n ( n + 1 ) \, ( 2 n + 1 ) \, a + \frac { 1 } { 4 } \, n ^ { 2 } ( n + 1 ) ^ { 2 } \, b & \\ & + \frac { 1 } { 3 } \sigma ^ { n } ( n + 1 ) \, ( 6 n ^ { 3 } + 9 n ^ { 2 } + n - 1 ) \, c = M _ { 2 } \\ \intertext { w h e r e } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { w h e r e } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s u n g a l l } \intertext { s$$

where M, M1, M2 denote the moments

(u1 + u2 + ... + un), (u1 + 2u2 + ... + nun), and (u1 + 22u2 + .. + n2un) of the ungraduated data. The three equations (11) determine a, b, c; the solution may conveniently be performed as follows :— Compute successively the numbers p, q, r, s, t, where

$$C o u p u l e s s i v e r y t h e n u m b e r s \, p , \, q , \, r , \, s , \, t , \, w h e r e \\ p = \frac { M _ { 0 } } { n } \, , \quad q = \frac { 2 M _ { 1 } } { n \, ( n + 1 ) } \, , \quad r = \frac { 6 M _ { 2 } } { n ( n + 1 ) } \, , \quad s = \frac { 6 \, ( q - p ) } { n - 1 } \, , \\ t = \frac { 2 \{ r - ( 2 n + 1 ) \, p \} } { n - 1 } \, .$$

Then c is given by

b is then given by

15 {t − (n + 1) s}

(n+2)(n−2)

b=s −(n+1)c

and a is then given by

a=q − 1 (2n+ 1) b −2n(n+ 1) c

... (12)


<!-- p:8 -->


The first of equations (11) may be used as a check.

Substituting the numerical values of a b c thus found in a :   ut  t a (n ttin x=1, 2, 3, ... in it, we obtain the numerical values of U'1,0, U2,0, 3,0, .. U'n,

Thus, performing the work in algebraical symbols for the case n=7, we find in this way

$$a = \frac { 1 } { 7 } M _ { 3 } - \frac { 9 } { 7 } M _ { 1 } + 1 7 M _ { 0 } \\ \therefore \frac { 1 } { 7 } M _ { 3 } - \frac { 9 } { 7 } M _ { 1 } + 1 7 M _ { 0 }$$

$$\begin{array} { r l } & { \frac { b = - \sin ^ { 8 } M _ { 2 } + \frac { 9 } { 3 } \sin ^ { 7 } M _ { 1 } - 4 M _ { 0 } } { c = 8 4 M _ { 2 } - 8 4 M _ { 1 } + \frac { 1 } { 4 } M _ { 0 } } } \\ & { \sigma = \sin ^ { 4 } M _ { 2 } - \sin ^ { 5 } M _ { 1 } + \frac { 1 } { 4 } M _ { 0 } } \end{array}$$

Substituting these values of a, b, c, in (10), we obtain

$$u _ { 1 0 } ^ { \prime } = \lambda _ { z } ( 3 2 u _ { 1 } + 1 5 u _ { 2 } + 3 u _ { 3 } - 4 u _ { 4 } - 6 u _ { 5 } - 3 u _ { 6 } + 5 u _ { 7 } )$$

and, similarly, for u'g, u'so, ... A check is afforded by verifying that the last equation may be written

$$\tilde { u } _ { 1 0 } ^ { \prime } - u _ { 1 } = \lim _ { \varphi \in \mathbb { Z } } ( 1 0 \Delta ^ { 3 } u _ { 1 } + 1 5 \Delta ^ { 3 } u _ { 2 } + 1 2 \Delta ^ { 3 } u _ { 3 } + 5 \Delta ^ { 3 } u _ { 4 } ) ,$$

since the values of u1o' - u1, u' - u2, .. thus found must always be expressible as linear combinations of the third differences of the ungraduated data.

Having thus found u'x,0 in terms of the ungraduated data, by substitution in equation (9) we obtain ∆"u'x-s,1 in terms of the ungraduated data. Denoting ∆3 u'z,, by vx, we therefore have ∆3v known; and from (3) and (4) we have

$$\Delta ^ { 3 } v _ { - 2 } = 0 , \quad \Delta v _ { - 1 } = 0 , \quad v _ { 0 } = 0 ,$$

so by mere summation of a difference-table we can obtain all the v's.

Then, continuing the literal working in the case n -7, we have

$$\Delta ^ { x } v _ { - 2 } = u _ { 1 0 } { ^ { \prime } } - u _ { 1 } = \lambda _ { 2 } ( 1 0 y _ { 1 } + 1 5 y _ { 2 } + 1 2 y _ { 3 } + 5 y _ { 4 } ) ,$$

where yx denotes ∆3ux; similarly

$$4 2 \, \Delta ^ { 3 } v _ { - 1 } = - 1 5 y _ { 1 } - 1 5 y _ { 2 } - 9 y _ { 3 } - 3 y _ { 4 }$$

$$4 2 \, \Delta ^ { 3 } v _ { 0 } = - 3 y _ { 1 } - 1 8 y _ { 2 } - 1 5 y _ { 3 } - 6 y _ { 4 } \, ,$$

and so on; writing these down in the ∆3 column of a difference-table, and forming the ∆2, Δ1, and ∆° columns by summation, we obtain the complete difference-table as follows :—


<!-- p:9 -->


A»

D

4

0


10y1+15y2+12ys+5y4

6y1+15ys + 18y3 + 3y4

3y1+9y2+15ys+15y4

0

h - - -h9 -  - - h -

-5y1-12y2-15y3-10y4

−5y1+3y3+2y4

10y1+15y2+12y3+5y4

- Z -8 - 1-

4y1+6y2−6y3−4y4

- ---

5y1+15y2+15y3+7y4

2y1+3y2−5y4

-3y1-3y2+3ys+3y4

−7y1−15y2- 15ys- 5y4

42v2=15y1+30y2+27y3+12y4 42+++=54 42v1=10y1+15yg+12ys+5y4 42v4=5y1+12ya+15ys+10y4

0

42v\_2=0

4=4-0

10y1+15y2+12ys+5y4

5y1+12y2+15y3+ 10y4

42v0=0

42vs=0

---1- The results ∆avs=0, ∆vg=0, vg=0, furnish a check on the accuracy of the working: and as a further check we may form the columns ∆4, ∆5, ∆o in thie difference-table: the column ∆° should give simply -42y1, -42yg, -42ys, –42y4.


<!-- p:10 -->


Having now obtained the numbers v1, v,, v3, v»\_3 we have to find the numbers u'i,1, u'2,1, ... u'n,, from them. For this we use the conditions that (1) u'x,1 satisfies the difference-equation

$$\Delta ^ { s } u _ { s , 1 } ^ { \prime } = v _ { s } \quad .$$

and (2) that it is the particular solution of this difference-equation for which the moments of orders 0, 1 and 2 vanish. So in order to compute u'x, 1, we write down v, , v, . v\_3 as the third column of a difference-table, and form the second, first and zero columns by summation, taking any arbitrary numbers whatever for the entries at the top of the columns. In this way we obtain in the zero column a set of numbers w1, wg, ... w, which satisfy the differenceequation (13). but which are not the particular solution we require. However, any two solutions of (13) differ only by a solution of the difference-equation ∆ay =0, i.e. they differ only by a quadratic function of x. So we can write

$$u _ { x , 1 } ^ { \prime } = & \, w _ { x } - A - B x - C x ^ { 2 } \ , \\$$

and we have now only to determine A, B and C. For this we use the second of the above conditions; denoting the sums

(w1 + w2 + ... + wn), (w1 + 2w2 + ... + nwn), (w1 + 22 wg + ... + n2wn) by No, N1, N2 respectively, we have by summing equation (14)

$$8 y \, 2 i _ { 0 } , \, N _ { 1 } , \, N _ { 2 } \, \text {respectively, } \, & w \, \text { have by summing equation } ( 1 ) \\ & n \, A + \frac { 1 } { 2 } \, n \, ( n + 1 ) \, B + \frac { 1 } { 6 } \, n \, ( n + 1 ) \, ( 2 n + 1 ) \, C = N _ { 0 } \\ & \frac { 1 } { 2 } \, n \, ( n + 1 ) \, A + \frac { 1 } { 6 } \, n \, ( n + 1 ) \, ( 2 n + 1 ) B \\ & + \frac { 1 } { 4 } n ^ { 2 } ( n + 1 ) ^ { 2 } \, C = N _ { 1 } \\ & \frac { 1 } { 6 } \, n \, ( n + 1 ) \, ( 2 n + 1 ) \, A + \frac { 1 } { 4 } n ^ { 2 } ( n + 1 ) ^ { 2 } B \\ & + \frac { 1 } { 3 } \frac { 1 } { 6 } \, n \, ( n + 1 ) \, ( 6 n ^ { 3 } + 9 n ^ { 2 } + n - 1 ) \, C = N _ { 2 } \\$$

$$\begin{array} { r l } & { \dot { n } \left ( n + 1 \right ) A + \frac { } { 6 } \dot { n } \left ( n + 1 \right ) \left ( 2 n + 1 \right ) B } \\ & { + \frac { } { 4 } n ^ { 2 } \left ( n + 1 \right ) ^ { \dagger } C = N _ { 1 } } \\ & { + \frac { } { 3 } n \left ( n + 1 \right ) \left ( 2 n + 1 \right ) A + \frac { 1 } { 4 } u ^ { 2 } \left ( n + 1 \right ) ^ { 2 } B } \\ & { + \frac { 1 } { 3 } \bar { \sigma } \left ( n + 1 \right ) \left ( 6 n ^ { 3 } + 9 n ^ { 2 } + n - 1 \right ) C = N _ { 2 } } \end{array}$$

These equations are of the same type as equations (1 l), and are solved in the same way ; that is we compute successively

$$P = \underline { N _ { 0 } } \, Q = - \frac { 2 N _ { 1 } } { \Omega ^ { 2 } } \cdot \Omega _ { 1 } = \underline { 6 \, N _ { 2 } } _ { 2 } \, \Omega _ { 2 } = \underline { 6 ( Q - P ) } \, \Omega _ { 2 } = \Omega _ { 1 }$$

then C is given by

$$P & = \frac { N _ { 0 } } { n } , \ Q = \frac { 2 N _ { 1 } } { n \left ( n + 1 \right ) } , \ R = \frac { 6 \left ( \tilde { X } _ { 2 } \right ) } { n \left ( n + 1 \right ) } , \ S = \frac { 6 ( Q - P ) } { n - 1 } \, , \\ & \quad T r = \frac { 2 \left \{ R - ( 2 n + 1 ) P \right \} } { n - 1 } \, , \\$$

B is given by and A is given by

$$C = \frac { 1 5 \{ T - ( n + 1 ) \mathcal { S } \} } { ( n + 2 ) \left ( n - 2 \right ) } \ . \\ B = S - ( n + 1 ) \ C$$

$$\stackrel { \stackrel { \cdot } { A } = Q - \frac { 1 } { 3 } ( 2 n + 1 ) \, B - \frac { 1 } { 2 } n ( n + 1 ) \, C . } \\$$

The first of equations (15) may be used as a check.


<!-- p:11 -->


Having thus found A, B, C we substitute in equation (14), and so calculate u'x, , for x = 1, 2, 3, ... n. Lastly, from the equation

$$u _ { x } ^ { ^ { \prime } } = u _ { z , \, 0 } ^ { ^ { \prime } } + \epsilon u _ { z , \, 1 } ^ { ^ { \prime } } \\ \, , \quad , \quad , \quad ,$$

we compute the graduated values u'x for x = 1, 2, ..., n. The graduation is thus completed.

The quantity €, which is at our disposal, is not selected until the end of the process, when we try two or three different values and see which gives the most satisfactory result. By increasing € we bring the graduated values into close fidelity to the ungraduated values, while by diminishing € we make the sequence of graduated values smoother. There is not much labour involved in these trials as they merely amount to multiplying the column of known values of u'x,, by the final value of €, and adding to the column of known values of u'x, o .

The advantages of this method of graduation seem to be

- (1) Its elasticity, due to the freedom of choice of €. A satisfactory method of graduation ought to possess such elasticity, because the degree to which we are justified in sacrificing fidelity in order to obtain smoothness varies greatly from one problem to another.
- (2) Its more logical basis in the mathematical theory of Probability.
- (3) The total of the u's and their first and second moments are the same in the graduated table as in the actual statistics on which it is based. (These conditions are not satisfied in methods such as Sheppard's or Spencer's, which depend on formulae for graduating individual values.)
- (4) It makes use of the whole material available to obtain each graduated value, whereas in e.g. Spencer's formula each value is graduated by using only it and its ten nearest neighbours on either side, and therefore the material used in order to graduate one value is slightly different from the material used in order to graduate the next member in the sequence.
- (5) There is no difficulty near the beginning and end of the sequence, whereas Spencer's formula cannot be applied when we are within ten places of either terminal.
- (6) These advantages are not counterbalanced by greater labour in the computations.


<!-- p:12 -->


§12. An example.

A short section of the Government Female Annuitants (1883) Ultimate Table is here graduated by (i) Spencer's formula (Journal of the Institute of Actuaries 38 (1904), p 334, 41 (1907), p 361), by (ii) Todhunter's method of interlaced parabolas (ibid 53 (1922) p. 92), iii) by the method of the present paper, taking ε=0 (iv), and taking € = 0·01, and (v) taking €=0·08.

|             |             |                                |                                            |                                            |                                                            |                                                     |                                                     |                                                   |                                                   |
|-------------|-------------|--------------------------------|--------------------------------------------|--------------------------------------------|------------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| - I         | Ungraduated | Graduate by Spencer's formulae | Graduated by Todhunter's i dhunters method | Graduated by Todhunter's i dhunters method | i Graduated ' by I the method ' ^ ; of th« paper ! withe=0 | Graduated \ hy the method of this paper with e=0-01 | Graduated \ hy the method of this paper with e=0-01 | Graduated by the method of this paper with e=0-08 | Graduated by the method of this paper with e=0-08 |
|             |             | q A 8                          | q                                          | A 8                                        | ! q A»                                                     | }                                                   | A 3                                                 | «                                                 | A 8                                               |
| 50          | 1019        | ! 1278                         | 1298                                       |                                            | 1244                                                       | 1219                                                |                                                     | 1048                                              |                                                   |
| 51 1550     |             | : 1332                         | 1391 -                                     | 1 3                                        | ! 1379                                                     | 1386                                                |                                                     | 1436                                              |                                                   |
| 1 52 ! 1611 | 551         | , ' 1494                       | 1497                                       | - 8                                        | 1504                                                       | 1525                                                | 4                                                   | 1673                                              | 16 42                                             |
| • 53 1753   | -204        | 1605                           | 1603                                       |                                            | 1620                                                       | 1640                                                | 3                                                   | 1775                                              |                                                   |
| i 54 1772   | -120 + 941  | - o 1707                       | 2 1701                                     | 6 &#124; - 4                               | &#124; 1727 !                                              | 1734                                                | 8 9                                                 | 1784                                              | 58 60                                             |
| 55 1548     | - 1271      | 1795                           | 5 1797                                     |                                            | 1824                                                       | 1 1815                                              |                                                     | 1758                                              |                                                   |
| 56 2022     | 591         | 1871 10                        | 1887                                       | 1 10                                       | 1911 -1                                                    | 1892                                                | 3 7                                                 | 1757                                              | 47 34                                             |
| 57 - 1923   | 550         | 1940                           | 8 1972                                     | 3                                          | 1989                                                       | 0 1968                                              | 1                                                   | 1828                                              | 17                                                |
| 58 1842     |             | 2012                           | 2062                                       |                                            | 2057                                                       | 2050                                                |                                                     | 2005                                              |                                                   |
| 59          | 2329        | 2095                           | 2160                                       |                                            | 2115                                                       | 2139                                                |                                                     | 2305                                              |                                                   |
| Sams        | 17369       | 17179                          | 17368                                      |                                            | 17370                                                      | 17368                                               |                                                     | 17369                                             |                                                   |


<!-- p:13 -->


The sum of the absolute values of the differences between the graduated and the corresponding ungraduated members is 1576 fooe       e rn nt method with €= 0, 1438 for the present method with € = 0·01, and 996 for the present method with € = 0 08. An examination of the figures shows that so far as smoothness alono is concerned the best result is obtained from the present method with €= 0 (as of course is inevitable) and that the graduated values thus obtained show a slightly a t t a st a t t at itn Spencer's or Todhunter's formula. If, however, we wish to attach more importance to fidelity, the new method with €=0 08 yields graduated values which are very much closer to the ungraduated values, and whose third differences are fairly regular and not very large.

一

二
