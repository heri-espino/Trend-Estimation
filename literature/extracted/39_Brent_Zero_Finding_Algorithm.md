---
id: "39_Brent_Zero_Finding_Algorithm"
source_pdf: "../pdf/39_Brent_Zero_Finding_Algorithm.pdf"
source_filename: "39_Brent_Zero_Finding_Algorithm.pdf"
format: "academic-paper"
extraction_profile: "text-math-tables-high-fidelity"
extraction_mode: "full-page-ocr"
extraction_quality: "excellent"
extraction_score: 106.0
visual_assets: "disabled"
references_file: "../references/39_Brent_Zero_Finding_Algorithm.references.md"
---

<!-- p:1 -->

## An algorithm with guaranteed convergence for finding a zero of a function

R. P. Brent*

Computer Science Department, Stanford University, Stanford, California 94305, USA

An algorithm is presented for finding a zero of a function which changes sign in a given interval. The algorithm combines linear interpolation and inverse quadratic interpolation with bisection. Convergence is usually superlinear, and is never much slower than for bisection. ALGOL 60 procedures are given.

(Received August 1970, Revised March 1971)

### 1. Introduction

Let f be a real-valued function, defined on the interval [a, b],

with f(a) f(b) ≤ 0. f need not be continuous on [a, b]: for example, f might be a limited-precision approximation to some continuous function (see Forsythe, 1969). We want to find an approximation ζ to a zero ζ of f, to within a given positive tolerance 2δ, by evaluating f at a small number of points. Of course, if f is discontinuous then there may be no zero in [a, b], so we shall be satisfied if f takes both non-negative and nonpositive values in [ζ − 2δ, ζ + 2δ] [a, b]. Clearly, such a ζ may always be found by bisection in about log2 [(b - a)/δ] steps, and this is the best that we can do for arbitrary f. We shall describe an algorithm which is never much slower than bisection, but which has the advantage of superlinear convergence to a simple zero ζ, if we ignore rounding errors and suppose that f is continuously differentiable near ζ. This means that, in practice, convergence is often much faster than for bisection.

### 2. Dekker's algorithm

The algorithm described here is similar to an algorithm, which we call Dekker's algorithm for short, variants of which have been given by van Wijngaarden, Zonneveld, and Dijkstra (1963), Wilkinson (1967), Peters and Wilkinson (1969), and Dekker (1969). We wish to emphasise that, although these variants of Dekker's algorithm have proved satisfactory in most practical cases, none of them guarantees convergence in less than about (b – a)/δ function evaluations (examples are given in Section 3 below). Our algorithm, on the other hand, must converge within about (log2 [(b − a)/δ])2 function evaluations. For example, typically we might have b - a = 1 and δ = 10−12, giving 1012 and 1,600 function evaluations respectively. On well-behaved functions, e.g. polynomials of moderate degree with well-separated roots, our algorithm has proved to be at least as fast as Dekker's, often slightly faster, so there is no extra price to pay for the improvement in the guaranteed rate of convergence. Of course, both our algorithm and Dekker's are much faster than bisection on well-behaved functions.

### 3. The algorithm

To avoid repetition, we assume that the reader is familiar with Peters and Wilkinson (1969) or Dekker (1969), and merely point out the differences between our algorithm and Dekker's. The algorithm is defined precisely by the ALGOL 60 procedure zero given in the Appendix.

mation so far to ζ, a is the previous value of b, and ζ must lie between b and c (initially a = c).

If f(b) ≠ 0 then let m = 1(c − b). We prefer not to return

If f(b) = 0 then we are finished (the ALGOL procedure given by Dekker (1969) does not recognise this case, and can take a large number of small steps if f vanishes on an interval, which may happen because of underflow).

with ζ = 1(b + c) as soon as |m| ≤ 2δ, for if superlinear con o  i     bs  ote approximation to ζ than ↓(b + c) is. Instead, we return with ζ = b if |m| ≤ δ (so the error is no more than δ if, as is often true, f is nearly linear between b and c), and otherwise interpolate (or extrapolate) f linearly between a and b, giving a new point i (see Section 4 for inverse quadratic interpolation). To avoid the possibility of overflow or division by zero we find i as b + p/q, and the division is not performed if 2|p| ≥ 3|m.q|, for then i is not needed anyway. The reason why the simpler criterion |p| ≥ |m.q| is not used is explained in Section 4. Since 0 &lt; |f(b)| ≤ |f(a)| (see Section 4), we can safely compute s = f(b)/f(a), p = ±(a − b)s, and q = 干(1 − s).

Define b′′ = Si if i lies between b and b + m ('interpolation'), b + m otherwise ('bisection'),

and

$$b ^ { \prime } = \begin{cases} b ^ { \prime } \text { if } | b - b ^ { \prime \prime } | > \delta , \\ b + \delta . \text { sign} ( m ) \text { otherwise} \end{cases}$$

Dekker's algorithm takes b' as the next point at which f is evaluated, forms a new set {a, b, c} from the old set {b, c, b′}, and continues. Unfortunately, it is easy to construct a function f for which steps of δ are taken every time, so about (b – a)/δ function evaluations are required for convergence. For example, let

b + δ. sign(m) otherwise (a 'step of δ').

$$) = \begin{cases} 2 ^ { x / \delta } \text { for } a + \delta \leqslant x \leqslant b , \\ - \left ( \frac { b - a - \delta } { \delta } \right ) . 2 ^ { b / \delta } \text { for } x = a , \end{cases}$$

The first linear interpolation gives the point b — δ, the next

(an extrapolation) gives b – 2δ, the next b — 3δ, and so on. Even if steps of δ are avoided, the asymptotic rate of convergence of successive linear interpolation may be very slow if f has a zero of sufficiently high multiplicity. An example for which convergence is worse than linear (Brent, 1971) is

$$\text {with} \quad \ f ( x ) = \begin{cases} 0 \text { if } x = 0 , \\ x . \exp \left ( - x ^ { - 2 } \right ) \text { if } x \neq 0 , \end{cases}$$

At a typical step we have three points a, b and c such that f(b). f(c) ≤ 0, |f(b)| ≤ |.f(c)|, and a may coincide with c. The points a, b and c change during the algorithm, but there should be no confusion if we omit subscripts. b is the best approxion an interval containing the origin. These examples are rather artificial, and unless an extended exponent range is used (see Section 8) we may be saved by underflow, but it is clear that with Dekker's algorithm convergence may occasionally be very slow.

Our main modification of Dekker's algorithm ensures that

*Present Address: P.O. Box 218, Yorktown Heights, New York 10598, USA.


<!-- p:2 -->


a bisection is done at least once in every 2.log2 (|b - cl/δ) consecutive steps. The modification is this: let e be the value of p/q at the step before the last one. If |e| &lt; δ or |p/q| ≥ łe| then we do a bisection, otherwise we do either a bisection or an interpolation just as in Dekker's algorithm. Thus le| decreases by at least a factor of two on every second step, and when le| &lt; δ a bisection must be done. Àfter a bisection we take e = m for the next step.

A simpler idea is to take e as the value of p/q at the last step, but this slows down convergence for well-behaved functions by causing unnecessary bisections. With the better choice of e, our experience has been that convergence is always at least as fast as for Dekker's algorithm.

### 4. Inverse quadratic interpolation

If the three current points a, b and c are distinct, we can find the point i by inverse quadratic interpolation, i.e. fitting x as a quadratic in y, instead of by linear interpolation using just a and b. For well-behaved functions this device saves about 0.5 u vge vaa  o v  e vttepolation is used because with direct quadratic interpolation we have to solve a quadratic equation for i. Cox (1970) gives another way of avoiding this problem. (See also Ostrowski (1966), Ch. 11.)

Care must be taken to avoid overflow or division by zero when computing the new point i. Since b is the most recent approximation to the root and a is the previous value of b, we do a bisection if |f(b)| ≥ |f(a)|. Otherwise we have |f(b)| &lt; |f(a)| ≤ If(c)|, so a safe way to find i is to compute

$$r _ { 1 } = f ( a ) / f ( c ) , r _ { 2 } = f ( b ) / f ( c ) , r _ { 3 } = f ( b ) / f ( a ) ,$$

and

$$r _ { 1 } = & \int ( a ) / ( c ) , r _ { 2 } = ) ( b ) / ( c ) , r _ { 3 } = ) ( b ) / ( a ) , \\ p = & \pm r _ { 3 } [ ( c - b ) \, r _ { 1 } ( r _ { 1 } - r _ { 2 } ) - ( b - a ) ( r _ { 2 } - 1 ) ] , \\ \text {and} & \quad q = \mp ( r _ { 1 } - 1 ) ( r _ { 2 } - 1 ) ( r _ { 3 } - 1 ) .$$

Then i = b + p/q, but as before we do not perform the division unless it is safe to do so (if bisection is to be done then i is not needed anyway). When inverse quadratic interpolation is used, the interpolating parabola cannot be a good approximation to f unless it is single-valued between (b, f(b)) and (c, f(c)), so it is natural to accept the point i if it lies between b and c and up to three-quarters of the way from b to c (consider the limiting case where the interpolating parabola has a vertical tangent at c and f(b) = −f(c)). Thus i will be rejected if

$$2 | p | \geqslant \frac { 3 } { 2 } \left | ( c - b ) q \right | .$$

### 5. Superlinear convergence

Ostrowski (1966) shows that if f is C2 in a neighbourhood of a simple zero ζ, then successive linear interpolation from a sufficiently good approximation gives superlinear convergence to ζ, with order at least ±(1 + √5) = 1·618 . . . . We remark that this result holds under the weaker hypothesis that f has a Lipschitz continuous derivative near ζ. In fact, convergence is superlinear, in the sense that lim |x − ζ|1/" = 0, if f is C1 n→∞

Ignoring the effect of rounding errors and the tolerance δ, we see, as in Dekker (1969), that the algorithm will eventually stop doing bisections when it is approaching a simple zero of a C1 function, so convergence will be superlinear. In practice, convergence for well-behaved functions is fast, and the stopping criterion is usually satisfied in a few steps once superlinear convergence sets in.

near ζ. If f' is Lipschitz continuous near ζ then the order is at least 1·618... when inverse quadratic interpolations are performed in place of some of the linear interpolations. For proofs of these results, see Brent (1971).

### 6. The tolerance

As in Peters and Wilkinson (1969), the tolerance (2δ) is a combination of a relative tolerance (4ε) and an absolute tolerance (2t). At each step we take δ = 2ε|b| + t, where b is the current best approximation to ζ, ε = macheps is the relative machine precision (β1-for τ-digit truncated floating-point arithmetic with base β, and half this for rounded arithmetic), and t is a positive absolute tolerance. Since δ depends on b, which could lie anywhere in the given interval, we should replace δ by its positive minimum over the interval in the upper bound for the number of function evaluations required. In the ALGOL procedures the variable tol is used for δ.

### 7. The effect of rounding errors

The ALGOL procedures have been written so that rounding errors in the computation of i, m etc. cannot prevent convergence with the above choice of δ. The number 2ε in the definition of δ (Section 6) may be increased if a higher relative error is acceptable, but it should not be decreased, for then rounding errors might prevent convergence.

The bound for |ζ — ζ has to be increased slightly if we take rounding errors into account. Suppose that, for floating-point numbers x and y, the computed arithmetic operations satisfy

and

$$\beta ( x \times y ) = x y ( 1 + \varepsilon _ { 1 } )$$

$$\gamma ( x \pm y ) = x ( 1 + \varepsilon _ { 2 } ) \pm y ( 1 + \varepsilon _ { 3 } ) ,$$

where |εi| ≤ ε for i = 1, 2 and 3 (see Wilkinson, 1963). We also assume that f(|x|) = |x| exactly, for any floating-point number x. The algorithm computes approximations

and

$$\tilde { m } = \beta ( 0 \cdot 5 \times ( c - b ) )$$

$$t \tilde { o } l = \beta ( 2 \times \varepsilon \times | b | + t )$$

to m and tol, where ζ lies between b and c, and the algorithm terminates with ζ = b only when

$$| \tilde { m } | \leqslant t \hat { o } l$$

(unless f(b) = 0, when ζ = ζ = b). Our assumptions give |m| ≥ {[|c − b| − ε(|b| + |c|)] (1 − ε),

and similarly

$$t \tilde { o } l \leq ( 2 \varepsilon | b | + t ) ( 1 + \varepsilon ) ^ { 3 } ,$$

$$\ t \tilde { l } \leq ( 2 \varepsilon | b | + t ) ( 1 + \varepsilon ) ^ { 3 } , \\ \text {agent} \quad \text {so } | \tilde { m } | \leq \ t \tilde { l } \text { implies that} \\ | c - b | \leq \left ( \frac { 2 } { 1 - \varepsilon } \right ) ( 2 \varepsilon | b | + t ) ( 1 + \varepsilon ) ^ { 3 } + \varepsilon ( | b | + | c | ) . \\ \text {Since } | \hat { \zeta } - \zeta | \leq | c - b | \text { and } b = \hat { \zeta } , \text { this gives} \\ | \hat { \zeta } - \zeta | \leq 6 \varepsilon | \zeta | + 2 t , \\ \text {neglecting terms of order } \text { and } \varepsilon ^ { 2 } | \zeta | . \text { Usually the error is less}$$

neglecting terms of order εt and ε2||. Usually the error is less than half this bound (see Section 3).

Of course, it is the user's responsibility to consider the effect of rounding errors in the computation of f. The ALGOL procedures only guarantee to find a zero ζ of the computed function f to the accuracy discussed above, and ζ may be nowhere near a root of the mathematically defined function that the user is really interested in.

### 8. Extended exponent range

In some applications the range of f may be larger than is allowed for standard floating-point numbers. Hence, in the Appendix we give an ALGOL procedure (zero2) which accepts f(x) represented as a pair (y(x), z(x)), where f(x) = y(x). 2z(x) (y real, z integer). Thus zero2 will accept functions in the same representation as is assumed by Peters and Wilkinson (1969), although zero2 does not require that 1/16 ≤ |y(x)| &lt; 1 (unless y(x) = 0), and could be simplified slightly if this assumption were made.


<!-- p:3 -->


### 9. Practical tests

The ALGOL procedures zero (for standard floating-point numbers) and zero2 (for floating-point with an extended exponent range) were tested using ALGOL W (Wirth and Hoare, 1966) on an IBM 360/67 and a 360/91 with machine precision 16-13 ≈ 2.5 × 10-16. The number of function evaluations for convergence was never more than three times greater than would be needed if bisection were used, even for the pathological functions given in Section 3, and for these functions Dekker's algorithm takes more than 106 function evaluations. Zero2 has been tested extensively with eigenvalue routines, and in this application it usually takes the same or one less function evaluation per eigenvalue than Dekker's algorithm, and considerably less than bisection (numerical results are given in Brent, 1971).

### 10. Concluding remarks

Our algorithm appears to be at least as fast as Dekker's on well-behaved functions, and, unlike Dekker's, it is guaranteed to converge in a reasonable number of steps for any function. The ALGOL procedures zero and zero2 given in the Appendix have been written to avoid problems with rounding errors or overflow, and floating-point underflow is not harmful as long as the result is set to zero. (A FORTRAN translation of procedure zero is given in Brent (1971).)

Finally, we note that golden section search and a method of successive parabolic interpolation (Jarratt, 1967) can be combined to give an algorithm for finding a local minimum of a function of one variable, just as bisection and successive linear interpolation can be combined to give an algorithm for finding a zero. The minimisation algorithm always converges nearly as fast as would Fibonacci search, and it converges superlinearly if f has a positive and continuous second derivative near the minimum (Brent, 1971).

A recent paper by Cox (1970) gives an algorithm which combines bisection with interpolation, using both f and f'. This algorithm may fail to converge in a reasonable number of steps in the same way as Dekker's. A simple modification, similar to the one that we have given in Section 3 for Dekker's algorithm, will remedy this defect without slowing the rate of convergence for well-behaved functions.

#### Acknowledgement

The author wishes to thank Professors G. E. Forsythe and G. H. Golub for their advice and encouragement, the referee for his helpful comments, and the CSIRO for its support.

## Appendix: Algol 60 procedures

real procedure zero (a, b, macheps, t, f); value a, b, macheps, t; real a, b, macheps, t; real procedure f; begin comment:

Procedure zero returns a zero x of the function f in the given interval [a, b], to within a tolerance 6macheps |x| + 2t, where macheps is the relative machine precision and t is a positive tolerance. The procedure assumes that f(a) and f(b) have different signs;

```
positive tolerance.  ' the procedure assumes that (/a) and (/b)
      have different signs;

      real c, d, e, fa, fb, fc, tol, m, p, q, r, s;
      fa := f(a); fb := f(b);
      int: c := a; fc := fa; d := e := b - a;
      ext: if abs(fc) < abs(fb) then
         begin a := b; b := c; c := a;
         fa := fb; fb := fc; fc := fa
         end;
      tol := 2 \times macheps \ abs(b) + t; m := 0-5 \times (c - b);
      if abs(m) > tol \fB \neq 0 then
```

begin comment: See if a bisection is forced;
  if abs(e) < tol \a abs(fa) < abs(fb) then d := e := m else
  extended begin s := fb/fa; if a = c then
    earth and
            begin comment: Linear interpolation;
            p := 2 × m × s; a := 1 - s
  function
    see times
  even for
    for these
    function
    genvalue
    or one
        q := (q - 1) × (r - 1) × (s - 1)
    s algor-
    results
            s := e; e := d;
            if 2 × p < 3 × m × q - abs(tol × q) ^
                                  p < abs(0:5 × s × q) then
  ker's on
    aranteed
    function
      a := b; fa := fb;
    popendix
    errors or
    as long
    of pro-
        end;
  such
    com-
    f'. This
    number of real procedure zero2 (a, b, macheps, t, f);
  department
    faction, value a, macheps, t; real a, b, macheps, t; procedure f;
  Dekker's
    rate of
      Procedure zero2 finds a zero of the function f' in the same
      way as procedure zero does, except that the procedure f(x, y, z)
  method of    returns  (real)  and  z (integer)  so  that f'(x) = y.2*.  Thus
  can .be     underflow  and  overflow  can be  avoided  with  a  very  large
  summ of     function range;

```

Procedure zero2 finds a zero of the function f in the same way as procedure zero does, except that the procedure f(x, y, z) returns y (real) and z (integer) so that f (x) = y.22. Thus underflow and overflow can be avoided with a very large function range;

real procedure pwr2 (x, n); value x, n; real x; integer n; comment: This procedure is machine-dependent. It computes x.2" for n ≤ 0, avoiding underflow in intermediate results;

```
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
```


<!-- p:4 -->


```
if p > 0 then q := -q else p := -p; s := e; e := d;
      if 2 < p < 3  x m \ x q - abs(tol \ x q)  \^
             p < abs(0-5 \ x s \ x q) then
      d := p/q else d := e := m
      end;
    a := b; fa := fb; ea := eb;
    b := b + (if abs(d) > tol then d else if m > 0 then
                  tol else -tol);
    f(b,fb,eb);
    go to if fb > 0 = fc < 0 then int else ext
    end;
  zero2 := b
  end zero2

References
```
