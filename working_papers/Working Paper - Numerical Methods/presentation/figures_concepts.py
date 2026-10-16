"""Six mathematical/pedagogical figures (not Monte Carlo evidence)."""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from _style import (
    BLUE, ORANGE, GREEN, PURPLE, GREY, BLACK, COLORS,
    canvas, finish, panel, annotate_kind,
)
from trend_estimation.core.pure import cached_pure_solver
from trend_estimation.core.smoothness import (
    lambda_to_smoothness, effective_degrees_of_freedom,
)
from trend_estimation.forecasting.operators import finite_difference_forecast_operator
from trend_estimation.forecasting.objectives import pure_forecast_loss_derivatives
from trend_estimation.core.smoothness import smoothness_to_lambda


def rolling_protocol():
    fig, (ax, ax2) = canvas(2, 1, title="01  |  Cómo se define F(S) mediante validación cronológica", height=7.5)
    for k, origin in enumerate((29, 36, 43)):
        y = 3 - k
        ax.add_patch(Rectangle((origin-23, y-.26), 23, .52, fc=BLUE, alpha=.82))
        ax.add_patch(Rectangle((origin, y-.26), 8, .52, fc=ORANGE, alpha=.85))
        ax.text(origin-11.5, y, "entrenamiento L", color="white", ha="center", va="center")
        ax.text(origin+4, y, "futuro h", color="white", ha="center", va="center", fontsize=9)
        ax.annotate("origen T", (origin, y+.28), (origin+1, y+.40), fontsize=9)
    ax.set(xlim=(0, 58), ylim=(0.5, 3.8), yticks=[1, 2, 3],
           yticklabels=["Pliegue 3", "Pliegue 2", "Pliegue 1"], xlabel="Índice temporal (ilustrativo)")
    ax.grid(axis="x", alpha=.15)
    panel(ax, "Ventanas móviles: validar solo bloques futuros ya observados")
    s = np.linspace(0, 1, 300)
    folds = [(.36+(s-.23)**2*.32), (.27+(s-.70)**2*.43), (.40+(s-.87)**2*.36)]
    for i, vals in enumerate(folds):
        ax2.plot(s, vals, color=COLORS[i], alpha=.7, lw=1.7, label=f"Pliegue {i+1}: f_T(S)")
    pooled = np.mean(folds, axis=0)
    ax2.plot(s, pooled, color=BLACK, lw=3, label="F(S) = pérdida media")
    panel(ax2, "El optimizador numérico trabaja con la pérdida combinada", "Suavizamiento normalizado S", "ECM ilustrativo")
    ax2.legend(ncol=4, fontsize=9, loc="upper center")
    return finish(fig, "01_rolling_cv_definition",
                  "El esquema y las curvas son ilustrativos; no representan resultados experimentales.")


def smoothing_family():
    n = 90
    t = np.arange(n)
    rng = np.random.default_rng(734)
    latent = .018*t + .00055*(t-42)**2 + .65*np.sin(t/15)
    observed = latent + rng.normal(0, .5, n)
    solver = cached_pure_solver(n, 2)
    fig, (ax, ax2) = canvas(1, 2, title="02  |  El suavizamiento cambia la tendencia estimada, no los datos observados")
    ax.scatter(t, observed, color=GREY, s=12, alpha=.45, label="Observaciones (ilustrativas)")
    ax.plot(t, latent, color=BLACK, ls="--", lw=2, label="Curva latente (conocida por construcción)")
    for s,c in zip((.25,.70,.95,1.0),COLORS):
        fitted=solver.fit_for_s(observed,s).trend
        ax.plot(t,fitted,lw=2,color=c,label=f"S = {s:g}")
    panel(ax,"Familia de tendencias estimadas","Índice de observación","Valor")
    ax.legend(fontsize=8, loc="upper left")
    ax2.plot(t, observed, ".", ms=2, color=GREY, alpha=.3)
    for s,c in zip((0.0,.7,.95,1.0),COLORS):
        fitted=solver.fit_for_s(observed,s).trend
        ax2.plot(t[-22:],fitted[-22:],lw=2.3,color=c,label=f"S = {s:g}")
    panel(ax2,"Detalle: nivel y pendiente al final","Índice de observación","Valor")
    ax2.legend(fontsize=9)
    return finish(fig, "02_smoothing_family",
                  "Serie pedagógica con semilla fija 734; no corresponde al estudio de simulación.")


def coordinate_map():
    n,d=63,2
    lam = np.logspace(-7,8,500)
    s = np.array([lambda_to_smoothness(float(x),n,d) for x in lam])
    fig,(ax,ax2)=canvas(1,2,title="03  |  De la penalización al dominio compacto de suavizamiento")
    ax.semilogx(lam,s,color=BLUE,lw=3)
    ax.axhline(1,color=ORANGE,ls=":",lw=1.7)
    ax.set(ylim=(-.02,1.04))
    panel(ax,"S(lambda) monótona","Penalización lambda (escala logarítmica)","S(lambda)")
    ds=np.diff(s)
    x=np.sqrt(lam[1:]*lam[:-1])
    ax2.semilogx(x,ds/np.diff(np.log(lam)),color=PURPLE,lw=2.5)
    panel(ax2,"Sensibilidad en la escala logarítmica de lambda","Penalización lambda (escala logarítmica)","dS / d log(lambda)")
    return finish(fig,"03_lambda_to_s",
                  "Calculado a partir del espectro de diferencias finitas con L=63 y d=2; extremos S(0)=0 y S(infinito)=1.")


def edf_geometry():
    n=63
    grid=np.linspace(0,1,401)
    fig,(ax,ax2)=canvas(1,2,title="04  |  Suavizamiento y grados de libertad efectivos")
    for d,c in zip((1,2,3,4),COLORS):
        df=n-(n-d)*grid
        ax.plot(grid,df,lw=2.3,label=f"d = {d}",color=c)
        ax2.plot(grid,df/n,lw=2.3,label=f"d = {d}",color=c)
        ax.scatter([1],[d],color=c,s=32)
    panel(ax,"Identidad exacta: EDF = L - (L-d)S","Suavizamiento normalizado S","EDF")
    panel(ax2,"Complejidad normalizada del modelo","Suavizamiento normalizado S","EDF / L")
    ax2.legend(fontsize=10)
    return finish(fig,"04_effective_degrees_of_freedom",
                  "Identidad del suavizador PLS con media cero; no equivale a grados de libertad de un estimador de mu dependiente de los datos.")


def endpoint_trends():
    n,h,d=70,15,2
    t=np.arange(n)
    rng=np.random.default_rng(509)
    observed=.04*t+.65*np.sin(t/9)+rng.normal(0,.35,n)
    solver=cached_pure_solver(n,d)
    G=finite_difference_forecast_operator(n,d,h).trend_matrix
    fig,(ax,ax2)=canvas(1,2,title="05  |  Modelos de frontera y extrapolación polinómica")
    ax.scatter(t, observed,s=13,alpha=.42,c=GREY,label="Observaciones")
    xf=np.arange(n,n+h)
    for s,c in ((0.,ORANGE),(.92,BLUE),(1.,GREEN)):
        fit=solver.fit_for_s(observed,s).trend
        ax.plot(t,fit,color=c,lw=2,label=f"S = {s:g}")
        ax.plot(np.r_[n-1,xf],np.r_[fit[-1],G@fit],color=c,lw=2,ls="--")
    ax.axvline(n-1,color=GREY,ls=":")
    panel(ax,"Ajuste y extrapolación natural con d=2","Índice de observación / pronóstico","Valor")
    ax.legend(fontsize=9,loc="upper left")
    for s,c in ((0.,ORANGE),(.92,BLUE),(1.,GREEN)):
        fit=solver.fit_for_s(observed,s).trend
        ax2.plot(t[-20:],fit[-20:],lw=2,color=c,label=f"S = {s:g}")
    ax2.set_xlim(n-21,n)
    panel(ax2,"Extremo del entrenamiento con mayor penalización","Índice","Tendencia estimada")
    ax2.legend(fontsize=9)
    return finish(fig,"05_exact_endpoints",
                  "Datos pedagógicos generados. S=0 implica H=I; S=1 es la proyección exacta sobre el núcleo de D_2.")


def fold_loss_geometry():
    h1=np.array([4,0,-2,-1,3,1],dtype=float)
    histories=[h1,h1+.5*np.array([0,1,0,-1,0,0]),h1+.15*np.arange(6)]
    targets=[np.array([0,1]),np.array([1,1.2]),np.array([-.5,0.5])]
    grid=np.linspace(0,.998,300)
    fig,(ax,ax2)=canvas(1,2,title="06  |  Combinar pérdidas históricas modifica la geometría")
    vals=[]
    for i,(hist,z) in enumerate(zip(histories,targets)):
        arr=np.array([pure_forecast_loss_derivatives(hist,z,order=2,
                     lambda_=smoothness_to_lambda(float(s),6,2)).value for s in grid])
        vals.append(arr)
        ax.plot(grid,arr,color=COLORS[i],lw=1.7,label=f"Origen {i+1}")
    pooled=np.mean(vals,axis=0)
    ax.plot(grid,pooled,lw=2.8,color=BLACK,label="Combinado")
    ax.legend(fontsize=9)
    panel(ax,"Pérdidas correspondientes a distintos orígenes","S","ECM a h pasos")
    ax2.plot(grid,pooled,color=BLACK,lw=2.7)
    j=int(np.argmin(pooled))
    annotate_kind(ax2,float(grid[j]),float(pooled[j]),"Mejor S de la malla",BLUE)
    ax2.set_xlim(0,1)
    panel(ax2,"Se buscan puntos estacionarios de la función combinada","S","ECM combinado")
    return finish(fig,"06_loss_pooling",
                  "Tres objetivos racionales ilustrativos; no corresponden al experimento de gran escala.")


FIGURES={
    "01_rolling_cv_definition":rolling_protocol,
    "02_smoothing_family":smoothing_family,
    "03_lambda_to_s":coordinate_map,
    "04_effective_degrees_of_freedom":edf_geometry,
    "05_exact_endpoints":endpoint_trends,
    "06_loss_pooling":fold_loss_geometry,
}
