"""Finite-difference nonzero-mean reconstruction, distinct from h-step CV.

D tau = mu*1 + eps. The analyst fixes order d (currently d=2 in
the experiment), and each pool shares ONE lambda. Statistical choices:

1. mu=0, the original model (misspecified if true mu != 0).
2. mu fixed externally (ORACLE only when true simulation mu supplied).
3. mu jointly estimated using observed data:
   (i) Gaussian differenced-contrast profile likelihood of mu,a,b;
   (ii) ordinary pooled leave-one-OBSERVATION-out PRESS with mu re-fitted
        within each training fold implicitly through the joint smoother.

The joint in-sample penalized mean fit is NOT the Guerrero sample-difference
plug-in and is NOT the forecast-horizon profiling of another working paper.

For finite lambda>0, p_j=comb(j,d), D p=1, H=(I+lambda Q)^-1,
T=Q H, b=T p, k=p.T b, ybar=mean_r y_r. Then
  mu_joint(lambda)=b.T ybar / k,
  fitted_r = H y_r + mu_joint (I-H) p.
The joint full-data hat matrix has within-series diagonal
H_ii + lambda * b_i^2/(R k). Thus the exact fold-local PRESS is:
  e_{ri} = [(T y_r)_i - b_i mu_joint] /
           [T_ii - b_i^2/(R k)].
The exact endpoints are continuous with scaled T at lambda=infinity.

Careful: there are effectively R*d+1 unpenalized dimensions as
lambda=infinity for pooled common mu, versus R*d in the fixed-mu model.
The nominal normalized S(lambda) remains a lambda coordinate and is
not the EDF of the whole estimated-mu smoothing procedure.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

import numpy as np
from scipy.optimize import minimize_scalar

from .objective import PooledLOOCV, difference_matrix, cached_difference_contrast_basis
from .variance_estimation import VarianceEstimate


@dataclass(frozen=True)
class FittedMeanVariance:
    mu: float
    variance: VarianceEstimate


def particular_polynomial(n: int, d: int) -> np.ndarray:
    """p_j=choose(j,d), with zero-indexed j, hence D_d p=1."""
    if not 1 <= d < n:
        raise ValueError("1 <= d < n required")
    return np.array([comb(i, d) for i in range(n)], dtype=float)


def fitted_affine_trend(base: PooledLOOCV, lam: float, mu: float):
    p = particular_polynomial(base.n, base.order)
    transformed = PooledLOOCV(base.y - mu * p[np.newaxis, :],
                               order=base.order)
    return transformed.trend(lam) + mu * p[np.newaxis, :]


class JointMeanPooledLOOCV:
    """Exact pooled leave-one-OBSERVATION-out CV for common fitted mu.

    Mu is the pooled joint-PLS parameter, reestimated within each
    deletion via the PRESS identity; never estimated using all data
    then falsely treated as fixed in validation.
    """

    def __init__(self, series: np.ndarray, order: int = 2):
        self.base = PooledLOOCV(series, order=order)
        self.y = self.base.y
        self.r, self.n, self.order = self.base.r, self.base.n, order
        self.p = particular_polynomial(self.n, order)
        self.up = self.base.u_positive.T @ self.p
        self.yn = self.base.uty
        self.calls_score = 0
        self.calls_derivative = 0

    def _parts(self, lam: float):
        if np.isnan(lam) or lam < 0:
            raise ValueError("lambda must be nonnegative")
        eig = self.base.eigenvalues
        # All numerator and denominator terms scale by the same factor
        # as lambda->infinity; choose unity for a stable limiting ratio.
        weights = (np.ones_like(eig) if np.isinf(lam)
                   else eig / (1.0 + lam * eig))
        u = self.base.u_positive
        b = u @ (weights * self.up)
        k = float(self.up @ (weights * self.up))
        t_y = u @ (weights[:, None] * self.yn)
        diagonal = self.base.u2 @ weights
        if k <= 0 or not np.isfinite(k):
            raise ArithmeticError("polynomial mean contrast is not identified")
        mu_hat = float(b @ np.mean(self.y, axis=0) / k)
        leverage_denom = diagonal - (b**2)/(self.r*k)
        if not np.all(leverage_denom > 0):
            raise ArithmeticError("deleted-observation fit not identified")
        return mu_hat, t_y, b, leverage_denom

    def fitted_mu(self, lam: float) -> float:
        return self._parts(float(lam))[0]

    def score(self, lam: float) -> float:
        self.calls_score += 1
        mu, t_y, b, diagonal = self._parts(float(lam))
        deleted_residuals = (t_y - b[:, None]*mu) / diagonal[:, None]
        return float(np.mean(deleted_residuals**2))

    def trend(self, lam: float) -> np.ndarray:
        mu = self.fitted_mu(lam)
        return fitted_affine_trend(self.base, float(lam), mu)

    def smoothness(self, lam: float) -> float:
        return self.base.smoothness(float(lam))

    def reset_counts(self):
        self.calls_score = 0
        self.calls_derivative = 0


def estimate_contrast_gaussian_mean(
        series: np.ndarray, difference: np.ndarray,
        fixed_mu: float | None = None, scan_points: int = 81) -> FittedMeanVariance:
    """Gaussian contrast ML of a=Var(eps), b=Var(eta), and optional mu.

    z_r=D y_r ~ N(mu*1, a I+b D D.T).
    For each covariance-mixing p, GLS-profile a COMMON mu if not fixed,
    then profile covariance scale; search p over [0,1] with endpoints.
    Exact global optimality is not claimed from a finite scan.
    """
    if scan_points < 5:
        raise ValueError("scan_points must be >= 5")
    y = np.asarray(series, dtype=float)
    if y.ndim == 1:
        y = y[np.newaxis, :]
    d = np.asarray(difference, dtype=float)
    if y.ndim != 2 or y.shape[1] != d.shape[1] or y.shape[0] < 1:
        raise ValueError("invalid y and difference matrix dimensions")
    if not np.isfinite(y).all():
        raise ValueError("data must be finite")
    if fixed_mu is not None and not np.isfinite(fixed_mu):
        raise ValueError("fixed mean must be finite")

    z = y @ d.T
    aa = d @ d.T
    eigvals, basis = (cached_difference_contrast_basis(y.shape[1], y.shape[1]-d.shape[0])
                      if np.array_equal(d, difference_matrix(y.shape[1], y.shape[1]-d.shape[0]))
                      else np.linalg.eigh(aa))
    if np.any(eigvals <= 0):
        raise ArithmeticError("D D.T must be positive definite")
    z_eig = z @ basis
    one_eig = basis.T @ np.ones(d.shape[0])
    normalizer = float(np.mean(eigvals))
    g_modes = eigvals/normalizer
    R,m = z_eig.shape

    def profile(p: float):
        g = (1.0-p) + p*g_modes
        if fixed_mu is None:
            denominator = float(np.sum(one_eig**2/g))
            if denominator <= 0:
                raise ArithmeticError("GLS mean not identified")
            mu = float(np.sum(np.mean(z_eig,axis=0)*one_eig/g) / denominator)
        else:
            mu = float(fixed_mu)
        centered = z_eig - mu*one_eig[None,:]
        power = np.mean(centered**2,axis=0)
        v = float(np.mean(power/g))
        if v <= 0 or not np.isfinite(v):
            return float("inf"), mu, v
        criterion = .5*(np.log(v)+float(np.mean(np.log(g)))+1.)
        return float(criterion), mu, v

    grid=np.linspace(0.,1.,scan_points)
    scores=np.array([profile(float(p))[0] for p in grid])
    candidates=[(scores[0],0.),(scores[-1],1.)]
    for i in range(1,len(grid)-1):
        if scores[i]<=scores[i-1] and scores[i]<=scores[i+1]:
            opt=minimize_scalar(
                lambda p: profile(float(p))[0],
                method="bounded",
                bounds=(float(grid[i-1]),float(grid[i+1])),
                options={"xatol":1e-12})
            if opt.success:
                candidates.append((float(opt.fun), float(opt.x)))
    _,pbest=min(candidates)
    _,mu,v=profile(float(pbest))
    a=v*(1.0-pbest)
    b=v*pbest/normalizer
    if not np.isfinite(a+b) or a<0 or b<0 or a+b<=0:
        raise ArithmeticError("invalid fitted variance components")
    ratio=b/a if a>0 else float("inf")
    estimate=VarianceEstimate(
        "gaussian_difference_gls_mean_ml" if fixed_mu is None
        else "gaussian_difference_fixed_mean_ml",
        float(b),float(a),float(ratio))
    return FittedMeanVariance(mu,estimate)
