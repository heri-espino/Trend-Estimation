"""Paper-faithful Cortes-Toto criteria with new pooled fitted-mean EDF.

The 2017 article compared CV, GCV, AICc and BIC with d=2 and mu=0;
our grouped R-series and unknown-common-mu extension is new code.
All smoke tests are deterministic and run in CI (no Monte Carlo campaign).
"""
import numpy as np
import pytest

from experiments.pooled_loocv_smoothness.cortes_optimality_criteria import (
    PenalizedCriteria, choose, CRITERIA
)
from experiments.pooled_loocv_smoothness.mean_difference_methods import (
    JointMeanPooledLOOCV, particular_polynomial
)
from experiments.pooled_loocv_smoothness.objective import (
    PooledLOOCV, difference_matrix
)


@pytest.mark.parametrize("d",[1,2,3,4])
@pytest.mark.parametrize("R",[1,3])
def test_cv_identical_to_original_press_and_joint_exact(d,R):
    rng=np.random.default_rng(2027100+100*d+R)
    y=rng.normal(size=(R,24))
    obj=PenalizedCriteria(y,order=d,mean_mode="zero")
    j=PenalizedCriteria(y,order=d,mean_mode="joint")
    old=PooledLOOCV(y,order=d)
    old_joint=JointMeanPooledLOOCV(y,order=d)
    for lam in (0.,.4,500.,float("inf")):
        assert obj.score("cv",lam)==pytest.approx(old.score(lam),rel=1e-10)
        assert j.score("cv",lam)==pytest.approx(old_joint.score(lam),rel=1e-10)
        assert np.isfinite(obj.score("gcv",lam))
        assert np.isfinite(j.score("gcv",lam))


@pytest.mark.parametrize("d",[1,2,3,4])
@pytest.mark.parametrize("R",[1,3])
def test_joint_edf_and_gcv_from_explicit_linear_hat_matrix(d,R):
    rng=np.random.default_rng(35000+2*d+R)
    n=25
    y=rng.normal(size=(R,n))
    obj=PenalizedCriteria(y,order=d,mean_mode="joint")
    D=difference_matrix(n,d)
    Q=D.T@D
    p=particular_polynomial(n,d)
    lam=2.
    H=np.linalg.solve(np.eye(n)+lam*Q,np.eye(n))
    T=Q@H
    b=T@p
    k=float(p@b)
    assert k>0
    allhat=np.kron(np.eye(R),H)+lam*np.kron(
        np.ones((R,R))/R, np.outer(b,b)/k)
    fit=(allhat@y.ravel()).reshape(R,n)
    rss=float(np.mean((y-fit)**2))
    edf=float(np.trace(allhat))
    assert obj.diagnostics(lam)["edf_total"]==pytest.approx(
        edf,rel=3e-6,abs=3e-6)
    assert obj.diagnostics(lam)["residual_mse"]==pytest.approx(
        rss,rel=3e-6,abs=3e-6)
    assert obj.score("gcv",lam)==pytest.approx(
        rss/(1.-edf/(R*n))**2,rel=3e-6,abs=3e-6)
    assert obj.score("aicc",lam)==pytest.approx(
        np.log(rss)+(2.*edf+1.)/(R*n-edf-2.),rel=3e-6,abs=3e-6)
    assert obj.score("bic",lam)==pytest.approx(
        np.log(rss)+edf*np.log(R*n)/(R*n),rel=3e-6,abs=3e-6)

    assert obj.diagnostics(0.)["edf_total"]==pytest.approx(R*n,abs=1e-5)
    assert obj.diagnostics(float("inf"))["edf_total"]==pytest.approx(R*d+1,abs=1e-6)


@pytest.mark.parametrize("d",[1,2,3,4])
def test_fixed_mu_shift_equivariance_under_known_exogenous_mean(d):
    rng=np.random.default_rng(5432+d)
    y=rng.normal(size=(3,28))
    p=particular_polynomial(28,d)
    mu=.25
    o=PenalizedCriteria(y,order=d,mean_mode="joint")
    s=PenalizedCriteria(y+mu*p,order=d,mean_mode="joint")
    fixed=PenalizedCriteria(y+mu*p,order=d,mean_mode="fixed",fixed_mu=mu)
    centered=PenalizedCriteria(y,order=d,mean_mode="zero")
    for name in CRITERIA:
        for lam in (.05,1.,1000.):
            assert o.score(name,lam)==pytest.approx(
                s.score(name,lam),abs=1e-5,rel=1e-5)
            assert fixed.score(name,lam)==pytest.approx(
                centered.score(name,lam),abs=1e-5,rel=1e-5)
    with pytest.raises(ValueError):
        PenalizedCriteria(y,order=d,mean_mode="fixed",fixed_mu=None)


def test_exact_smoothness_endpoints_fixed_and_joint():
    rng=np.random.default_rng(8899)
    y=rng.normal(size=(3,30))
    for mode in ("zero","joint"):
        obj=PenalizedCriteria(y,order=2,mean_mode=mode)
        for smoothness in (0.,.2,.8,.95,1.):
            result=obj.choose_fixed_smoothness(smoothness)
            assert result.smoothness==pytest.approx(smoothness,abs=1e-8)
            assert result.edf_total<=obj.N+1e-8
            assert np.isfinite(result.mu_fit)
            assert np.all(np.isfinite(obj.trend(result.lam)))


def test_aicc_excludes_near_interpolation_bic_has_truncation_caveat():
    y=np.random.default_rng(772).normal(size=(1,25))
    obj=PenalizedCriteria(y,order=2,mean_mode="joint")
    assert np.isinf(obj.score("aicc",0.))
    assert np.isinf(obj.score("bic",0.))
    assert np.isfinite(obj.score("gcv",0.))
    assert np.isfinite(obj.score("gcv",float("inf")))
    near=obj.score("bic",1e-6)
    far=obj.score("bic",1e-2)
    assert near<far  # reproduces plain logRSS BIC near-interpolation issue


@pytest.mark.parametrize("name",CRITERIA)
@pytest.mark.parametrize("mode",["zero","joint"])
def test_numerical_search_reports_criterion_and_mu_selection(name,mode):
    rng=np.random.default_rng(555)
    y=rng.normal(size=(3,24))
    obj=PenalizedCriteria(y,order=2,mean_mode=mode)
    a=choose(obj,name,solver="multibracket",scan_points=25)
    assert a.criterion==name
    assert a.mean_mode==mode
    assert a.evaluated>0
    assert a.lam>=0
    assert np.isfinite(a.score)
    assert 0<=a.smoothness<=1
    assert 0 < a.edf_total <= obj.N
    if name=="bic":
        assert a.boundary != "exact_zero"


def test_guerrero_original_S_vs_normalized_project_coordinate():
    obj=PenalizedCriteria(np.random.default_rng(1).normal(size=(3,40)),
                          order=3,mean_mode="zero")
    result=obj.choose_fixed_smoothness(.7)
    paper_index=(obj.n-obj.d)*result.smoothness/obj.n
    Htrace=obj.d+sum(1/(1+result.lam*obj.raw.eigenvalues))
    assert paper_index==pytest.approx(1-Htrace/obj.n,rel=1e-9)
