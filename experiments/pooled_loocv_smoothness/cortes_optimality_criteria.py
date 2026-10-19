"""Cortes-Toto, Guerrero & Reyes (2017) PLS selector criteria, extended to pooled R and d=1..4.

Source: "Trend smoothness achieved by penalized least squares with the
smoothing parameter chosen by optimality criteria" (2017), sec. 2:
CV (eq. 17), GCV (18), AICc (22), BIC (21), controlled smoothness (9).
They study d=2, mu=0; the general R-series shared-mean extension BELOW
is OUR extension, not a direct implementation from that publication.

IMPORTANT separation:
- Statistical SCORE: CV, GCV, AICc, BIC, or EXOGENOUS fixed smoothness.
- Nuisance mean: fixed 0, externally fixed (known true in simulations),
  or fitted common mean *inside each PLS fit* (joint).
- Numerical search: finite grid/refinement, bounded scalar minimizer.
- Gaussian GLS mean/variance ML is a separate statistical criterion.

For joint common-mu PLS, the full RN x RN linear smoother has diagonal
block H + lambda*b*b.T/(R*k), off-diagonal blocks
lambda*b*b.T/(R*k), with b=T p, k=p.T T p,
T=Q (I+lambda Q)^-1 and p_t=choose(t,d).
Its total EDF equals R*tr(H)+lambda*||b||²/k, and the
pooled GCV denominator uses total EDF/(RN), NOT tr(H)/N.
This is derived here, not attributed to Cortes-Toto et al.

Known/fixed mu scores condition on externally chosen mu. Do NOT pass
all-data plug-in mu to "fixed" CV/GCV and label the score deletion-clean:
that freezes information from the held-out observation.

AICc is undefined if RN - EDF <= 2; return +infinity.
Plain BIC based on log(RSS) is unbounded below toward interpolating
lambda->0 for a noise-free interpolating linear smoother. Therefore BIC
is searched on an EXPLICITLY FINITE positive lambda domain ONLY and
boundary solutions must be flagged. Its boundary result must not be
reported as an unconstrained optimal smoothing parameter.
AIC (uncorrected) is source-discussed but was excluded from their
final simulation due to unreliable numerical behavior; not promoted.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import log
from typing import Literal

import numpy as np
from scipy.optimize import brentq, minimize_scalar

from .mean_difference_methods import JointMeanPooledLOOCV, particular_polynomial
from .objective import PooledLOOCV

Criterion = Literal["cv", "gcv", "aicc", "bic"]
MeanMode = Literal["zero", "fixed", "joint"]
CRITERIA: tuple[str, ...] = ("cv", "gcv", "aicc", "bic")
MEAN_MODES: tuple[str, ...] = ("zero", "fixed", "joint")


@dataclass(frozen=True)
class SelectorResult:
    criterion: str
    mean_mode: str
    solver: str
    lam: float
    score: float
    smoothness: float
    mu_fit: float
    edf_total: float
    evaluated: int
    boundary: str | None
    domain_log_min: float
    domain_log_max: float


class PenalizedCriteria:
    """Observed series as R x N; compares criteria within identical data."""

    def __init__(self, series: np.ndarray, order: int = 2,
                 mean_mode: MeanMode = "zero", fixed_mu: float | None = None):
        if mean_mode not in MEAN_MODES:
            raise ValueError("mean_mode must be zero, fixed or joint")
        if mean_mode == "fixed" and (
            fixed_mu is None or not np.isfinite(fixed_mu)):
            raise ValueError("fixed_mu must be external and finite")
        if mean_mode != "fixed" and fixed_mu is not None:
            raise ValueError("Only mean_mode=fixed accepts fixed_mu")
        self.raw = PooledLOOCV(series, order=order)
        self.n = self.raw.n
        self.R = self.raw.r
        self.N = self.n*self.R
        self.d = order
        self.mean_mode = mean_mode
        self.fixed_mu = 0. if mean_mode == "zero" else (
            float(fixed_mu) if mean_mode == "fixed" else None)
        self.p = particular_polynomial(self.n,order)
        self.u = self.raw.u_positive
        self.uty = self.raw.uty
        self.up = self.u.T @ self.p
        self.joint = JointMeanPooledLOOCV(series,order) if mean_mode == "joint" else None
        if mean_mode == "joint":
            self.projected = self.uty
            self.cv_object = self.joint
        else:
            self.projected = self.uty - self.up[:,None]*self.fixed_mu
            shifted = self.raw.y - self.fixed_mu*self.p[None,:]
            self.cv_object = PooledLOOCV(shifted,order)
        self.calls = 0

    def _components(self, lam: float):
        if np.isnan(lam) or lam < 0:
            raise ValueError("lambda must be >=0")
        eig = self.raw.eigenvalues
        if np.isinf(lam):
            weights=np.ones_like(eig)  # scaled lambda*T limit
            trH=float(self.d)
            scale=1.
        else:
            weights=eig/(1.+lam*eig)
            trH=float(self.d+np.sum(1./(1.+lam*eig)))
            scale=lam
        if self.joint is None:
            numerator = self.u @ (weights[:,None]*self.projected)
            mu=float(self.fixed_mu)
            edf=self.R*trH
            t_trace=float(np.sum(weights))
        else:
            b=self.u @ (weights*self.up)
            k=float(self.up@(weights*self.up))
            if not (k>0 and np.isfinite(k)):
                raise ArithmeticError("unidentifiable common PLS difference mean")
            mu=float(b@np.mean(self.raw.y,axis=0)/k)
            numerator=self.u @ (weights[:,None]*self.uty)-b[:,None]*mu
            edf=self.R*trH+scale*float(b@b)/k
            t_trace=float(np.sum(weights))-float(b@b)/(self.R*k)
        # numerator is scaled (I-S)y / lambda at finite lambda.
        return numerator,mu,edf,t_trace,scale

    def diagnostics(self,lam:float):
        numerator,mu,edf,t_trace,scale=self._components(float(lam))
        return {
            "fitted_mu":mu,
            "edf_total":float(edf),
            "residual_mse":float(np.mean((scale*numerator)**2)),
            "gcv_score":float(np.mean(numerator**2)/(t_trace/self.n)**2),
        }

    def score(self,criterion:Criterion,lam:float)->float:
        if criterion not in CRITERIA:
            raise ValueError("Only CV,GCV,AICc,BIC are literature criteria")
        self.calls+=1
        if criterion=="cv":
            return float(self.cv_object.score(float(lam)))
        numerator,_,df,t_trace,scale=self._components(float(lam))
        if criterion=="gcv":
            if t_trace <=0: return float("inf")
            return float(np.mean(numerator**2)/(t_trace/self.n)**2)
        if criterion=="aicc" and self.N-df<=2.+1e-10:
            return float("inf")
        if lam == 0.:
            # As lambda approaches 0, RSS->0; unrestricted BIC is
            # unbounded and must be explicitly constrained.
            return float("inf")
        rss=float(np.mean((scale*numerator)**2))
        if not (rss>0 and np.isfinite(rss)):
            return float("inf")
        if criterion=="aicc":
            # Cortes-Toto et al. (2017), eq 22, replacing N, df
            # with total pooled observation count and JOINT EDF.
            return float(np.log(rss)+(2.*df+1.)/(self.N-df-2.))
        if criterion=="bic":
            # Eq 21, apart from constants independent of lambda.
            return float(np.log(rss)+df*np.log(self.N)/self.N)
        raise AssertionError("not reached")

    def trend(self,lam:float):
        if self.joint is not None:
            return self.joint.trend(lam)
        from .mean_difference_methods import fitted_affine_trend
        return fitted_affine_trend(self.raw,lam,float(self.fixed_mu))

    def smoothness(self,lam:float):
        return self.raw.smoothness(lam)

    def choose_fixed_smoothness(self,s:float)->SelectorResult:
        """Controlled percentage: user PREDECLARES s, no data-driven tuning."""
        if not 0.<=s<=1.:
            raise ValueError("normalized smoothness target must be in [0,1]")
        if s==0.:
            lam=0.
        elif s==1.:
            lam=float("inf")
        else:
            lo,hi=-50.,50.
            def fn(x):return self.smoothness(float(np.exp(x)))-s
            if fn(lo)>0 or fn(hi)<0:
                raise ValueError("smoothness root outside bracket")
            lam=float(np.exp(brentq(fn,lo,hi,xtol=1e-11)))
        comp=self.diagnostics(lam)
        return SelectorResult("controlled_smoothness",self.mean_mode,
                              "inverse_smoothness",lam,s,self.smoothness(lam),
                              comp["fitted_mu"],comp["edf_total"],
                              0,None,-50.,50.)


def choose(obj:PenalizedCriteria,criterion:Criterion,
           *,solver:Literal["multibracket","bounded"]="multibracket",
           log_bounds=(-20.,35.),scan_points:int=81,
           xatol=1e-10)->SelectorResult:
    """Reproducible numerical candidate search, NOT global certificate.

    Both endpoints are compared for CV/GCV/AICc (when finite);
    BIC has lambda=0 excluded because its logRSS limit is -infinity.
    multibracket scans local score minima then Brent-refines each
    bracket; bounded uses one local bounded minimization.
    """
    if criterion not in CRITERIA:
        raise ValueError("criterion must be among CV/GCV/AICc/BIC")
    if solver not in ("multibracket","bounded") or scan_points<5:
        raise ValueError("unknown solver or too few scan points")
    lb,ub=map(float,log_bounds)
    if not (np.isfinite(lb) and np.isfinite(ub) and lb<ub):
        raise ValueError("log_bounds must be ordered finite numbers")
    obj.calls=0
    def f(x):
        return obj.score(criterion,float(np.exp(x)))
    if solver=="bounded":
        minim=minimize_scalar(f,method="bounded",bounds=(lb,ub),
                              options={"xatol":xatol})
        candidates=[(float(minim.fun),float(minim.x))]
    else:
        grid=np.linspace(lb,ub,scan_points)
        values=[f(float(v)) for v in grid]
        candidates=[(values[0],lb),(values[-1],ub)]
        for i in range(1,scan_points-1):
            if (np.isfinite(values[i]) and
                values[i] <= values[i-1] and
                values[i] <= values[i+1]):
                local=minimize_scalar(f,method="bounded",
                    bounds=(float(grid[i-1]),float(grid[i+1])),
                    options={"xatol":xatol})
                if local.success and np.isfinite(local.fun):
                    candidates.append((float(local.fun),float(local.x)))
    for lam in (0.,float("inf")) if criterion!="bic" else (float("inf"),):
        value=obj.score(criterion,lam)
        if np.isfinite(value):
            candidates.append((value,lam))
    best_val,best_x=min(candidates,key=lambda k:k[0])
    best_lam=best_x if best_x in (0.,float("inf")) else float(np.exp(best_x))
    if best_x==0.:bound="exact_zero"
    elif np.isinf(best_x):bound="exact_infinity"
    elif abs(best_x-lb)<1e-5:bound="truncated_lower_lambda_limit"
    elif abs(best_x-ub)<1e-5:bound="truncated_upper_lambda_limit"
    else:bound=None
    # NOTE: when criterion BIC, even an apparent interior best is only
    # finite-domain minimum: source BIC has no unconstrained optimum.
    diagnostics=obj.diagnostics(best_lam)
    return SelectorResult(criterion,obj.mean_mode,solver,best_lam,
        float(best_val),obj.smoothness(best_lam),diagnostics["fitted_mu"],
        diagnostics["edf_total"],obj.calls,bound,lb,ub)
