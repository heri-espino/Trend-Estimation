"""Search geometry, derivations, stepwise algorithm, adversarial examples."""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from _style import BLUE, ORANGE, GREEN, PURPLE, GREY, BLACK, COLORS
from _style import canvas, finish, panel, annotate_kind, frozen_csv
from trend_estimation.core.smoothness import smoothness_to_lambda, lambda_to_smoothness
from trend_estimation.forecasting.objectives import pure_forecast_loss_derivatives
from trend_estimation.selection.smoothness_numerical import find_stationary_points_smoothness
from trend_estimation.benchmarks.adversarial import adversarial_smoothness_cases

X=np.array([4.,0.,-2.,-1.,3.,1.])
Z=np.array([0.,1.])
ROOT_LAMBDA=(0.146706269970,1.101542792611,31.808860111816)
ROOT_S=(0.380475,0.718759,0.976961)
ROOT_KINDS=("minimum","maximum","minimum")


def callback(lam):
    z=pure_forecast_loss_derivatives(X,Z,order=2,lambda_=float(lam))
    return z.value,z.first,z.second


def curve(n=601):
    grid=np.linspace(0.,.998,n)
    lam=[smoothness_to_lambda(float(s),6,2) for s in grid]
    derivatives=np.array([callback(x) for x in lam])
    sder=np.array([
        _sder(x) for x in lam
    ])
    first=derivatives[:,1]/sder[:,0]
    second=derivatives[:,2]/sder[:,0]**2-derivatives[:,1]*sder[:,1]/sder[:,0]**3
    return grid,derivatives[:,0],first,second


def _sder(lam):
    from trend_estimation.core.smoothness import smoothness_derivatives
    return smoothness_derivatives(lam,6,2)


def derivative_profiles():
    s,f,d1,d2=curve()
    fig,axs=canvas(3,1,title="07  |  Función objetivo, derivada y curvatura",height=9.4)
    for ax,y,label,color in zip(axs,(f,d1,d2),("F(S)","dF/dS","d²F/dS²"),(BLUE,ORANGE,PURPLE)):
        ax.plot(s,y,color=color,lw=2.2)
        for j,root in enumerate(ROOT_S):
            ax.axvline(root,color=GREEN if j!=1 else GREY,alpha=.5,ls="--")
        if label!="F(S)": ax.axhline(0,color=BLACK,lw=.9,alpha=.5)
        panel(ax,label,"Suavizamiento normalizado S",label)
        ax.set_xlim(0,1)
        # Symmetric clipping only when the endpoint transformation exaggerates curvature.
        if label=="d²F/dS²":
            lo,hi=np.percentile(y,[1,99])
            if lo<hi: ax.set_ylim(lo-abs(lo)*.15,hi+abs(hi)*.15)
    return finish(fig,"07_objective_derivative_curvature",
                  "Ejemplo racional exacto de seis observaciones; curvas evaluadas numéricamente fuera de S=1.")


def adaptive_steps():
    results=find_stationary_points_smoothness(callback,n_obs=6,order=2)
    s,f,_,_=curve(401)
    hi=1-1e-6
    initial=np.linspace(0,hi,9)
    skeleton=set(float(v) for v in initial)
    width=float(initial[1]-initial[0])
    for k in range(1,7):
        offset=width/(2**k)
        skeleton.add(offset);skeleton.add(hi-offset)
    all_samples=np.array(results.sampled_smoothness_)
    points=results.points_
    roots=[p.smoothness_ for p in points]
    panels=[
        ("1. Malla inicial",initial),
        ("2. Refuerzo de extremos",np.array(sorted(skeleton))),
        ("3. Subdivisión adaptativa",all_samples),
        ("4. Intervalos y muestras",all_samples),
        ("5. Raíces refinadas con Brent",np.array(roots)),
        ("6. Comparar con los extremos",np.array(roots+[0,1])),
    ]
    fig,axs=canvas(2,3,title="08  |  Etapas de la búsqueda adaptativa en S",height=8.3)
    yrange=float(f.max()-f.min())
    for k,(ax,(name,samples)) in enumerate(zip(axs,panels)):
        ax.plot(s,f,color=BLUE,lw=2)
        if k<=3:
            show=samples
            if k==3:
                show=all_samples[::max(1,len(all_samples)//110)]
            yy=np.interp(np.clip(show,0,.998),s,f)
            ax.scatter(show,yy,color=ORANGE,s=12 if k>=2 else 35,alpha=.8,zorder=5)
        if k>=3:
            for pt in points:
                ax.scatter(pt.smoothness_,pt.objective_,s=60,color=GREEN if pt.kind_=="minimum" else PURPLE,edgecolor="white",zorder=6)
        if k==5:
            for x in (0,1):ax.axvline(x,color=BLACK,ls=":",lw=1.6)
            ax.text(.02,float(f.max())-.08*yrange,"extremos incluidos",fontsize=9,color=GREY)
        ax.set_xlim(-.01,1.01)
        panel(ax,name,"S","F(S)")
        if k!=5:ax.set_ylim(f.min()-.08*yrange,f.max()+.12*yrange)
    return finish(fig,"08_adaptive_search_steps",
                  f"Pérdida PLS de ejemplo; las muestras se reconstruyen a partir del resultado final (n={results.n_evaluations_}); no es un registro cronológico.")


def endpoint_failure():
    data=frozen_csv("sensitivity","sensitivity_cases.csv")
    fail=data.loc[(data["parameter"].eq("endpoint_refinement_levels")) &
                  (data["setting"].astype(str).eq("0")) &
                  (data["missed_minima"]>0)].copy()
    if fail.empty:
        raise ValueError("Frozen sensitivity file has no endpoint-disabled failure case.")
    key=["seed","scenario","order","window","horizon"]
    primary=data.loc[data["is_primary"].astype(str).str.lower().eq("true")]
    selected=fail.iloc[0]
    mask=np.logical_and.reduce([primary[c].eq(selected[c]) for c in key])
    normal=primary.loc[mask]
    if len(normal)!=1:
        raise ValueError("Cannot match frozen primary specification to boundary failure.")
    ref=normal.iloc[0]
    fig,axs=canvas(1,2,title="09  |  Qué evita el refinamiento cerca de los extremos")
    ax=axs[0]
    positions=[float(selected["best_s"]),float(ref["best_s"]),float(ref["dense_best_s"])]
    for y,(x,label,color) in enumerate(zip(positions,("Sin refinamiento","Método fijado","Malla densa"),(ORANGE,BLUE,GREEN))):
        ax.scatter([x],[2-y],s=150,color=color,zorder=3)
        ax.text(x+.003,2-y,label,va="center",fontsize=11,color=color)
    panel(ax,"Valor de S elegido en un caso problemático","S seleccionado","")
    ax.set(ylim=(-.6,2.6),yticks=[],xlim=(max(0,min(positions)-.05),min(1,max(positions)+.13)))
    ax2=axs[1]
    settings=frozen_csv("sensitivity","sensitivity_summary.csv")
    show=settings.loc[settings["parameter"].isin(("primary","endpoint_refinement_levels"))].copy()
    show=show.sort_values("mean_evaluations")
    labels=["principal" if x=="primary" else f"niveles={y}" for x,y in zip(show["parameter"],show["setting"])]
    ax2.barh(labels,show["missed_minima"],color=[BLUE if x=="primary" else ORANGE for x in show["parameter"]])
    panel(ax2,"Mínimos de referencia no detectados en 216 casos","Número no detectado","")
    ax2.invert_yaxis()
    fig.text(.05,.06,f"Caso seleccionado: semilla={selected['seed']}, { {'baseline':'base','persistent':'persistente','rough':'irregular'}.get(selected['scenario'], selected['scenario']) }, "
             f"d={selected['order']}, L={selected['window']}, h={selected['horizon']}",fontsize=9,color=GREY)
    return finish(fig,"09_endpoint_refinement_ablation",
                  "Valores leídos directamente del análisis de sensibilidad; no reconstruyen un historial de búsqueda.")


def sturm_landscape():
    s,f,g,_=curve(801)
    fig,axs=canvas(1,2,title="10  |  Conteo exacto de raíces; posiciones aproximadas")
    axs[0].plot(s,f,color=BLUE,lw=2.4)
    for k,(x,kind) in enumerate(zip(ROOT_S,ROOT_KINDS)):
        y=callback(ROOT_LAMBDA[k])[0]
        annotate_kind(axs[0],x,y,f"r{k+1}: {'mínimo' if kind == 'minimum' else 'máximo'}",GREEN if kind=="minimum" else ORANGE)
    annotate_kind(axs[0],0,callback(0.)[0],"S=0",BLACK)
    annotate_kind(axs[0],1,169/441,"S=1",BLACK)
    panel(axs[0],"F(S): mínimo / máximo / mínimo","S","ECM de pronóstico")
    axs[0].set_xlim(-.03,1.05)
    axs[1].plot(s,g,color=PURPLE,lw=2.1)
    axs[1].axhline(0,color=BLACK,lw=1.0)
    for k,x in enumerate(ROOT_S):
        axs[1].axvline(x,color=GREEN if k!=1 else ORANGE,ls="--",lw=1.5)
    panel(axs[1],"F'(S): exactamente tres raíces estacionarias positivas","S","Derivada")
    axs[1].set_xlim(0,1)
    return finish(fig,"10_sturm_worked_example",
                  "Conteo exacto de Sturm V(0+)-V(infinito)=5-2=3; las posiciones dibujadas son aproximaciones numéricas.")


def lambda_view():
    s,f,_,_=curve(701)
    lam=np.array([smoothness_to_lambda(float(x),6,2) for x in s])
    fig,axs=canvas(1,2,title="11  |  Una misma geometría de pérdida en lambda y S")
    axs[0].semilogx(np.maximum(lam,1e-7),f,color=ORANGE,lw=2.4)
    for x in ROOT_LAMBDA:axs[0].axvline(x,color=GREY,ls=":")
    panel(axs[0],"Penalización original (escala logarítmica)","lambda","ECM de pronóstico")
    axs[1].plot(s,f,color=BLUE,lw=2.4)
    for x in ROOT_S:axs[1].axvline(x,color=GREY,ls=":")
    panel(axs[1],"Coordenada normalizada de suavizamiento","S","ECM de pronóstico")
    axs[1].set_xlim(0,1)
    return finish(fig,"11_lambda_vs_s_landscape",
                  "Ambos paneles corresponden a un mismo ejemplo racional de seis observaciones; no comparan optimizadores.")


def adversarial_gallery():
    cases=adversarial_smoothness_cases()
    grid=np.linspace(0,1,801)
    fig,axs=canvas(3,3,title="12  |  Geometrías difíciles del banco adversarial",height=9.5)
    for ax,case in zip(axs,cases):
        vals=np.array([case.value(float(x)) for x in grid])
        ax.plot(grid,vals,color=BLUE,lw=2)
        minima=list(case.true_minima)+list(case.true_flat_minima)
        boundary=list(case.true_boundary_minima)
        if minima:
            ax.scatter(minima,[case.value(x) for x in minima],color=GREEN,s=35,zorder=5)
        if boundary:
            ax.scatter(boundary,[case.value(x) for x in boundary],color=ORANGE,s=35,zorder=5)
        panel(ax,{"near_zero":"cerca de cero","near_one":"cerca de uno","close_pair":"mínimos próximos","close_upper_pair":"par en el extremo","flat_minimum":"mínimo plano","stationary_inflection":"inflexión estacionaria","five_minima":"cinco mínimos","boundary_zero":"extremo S=0","boundary_one":"extremo S=1"}.get(case.name,case.name.replace("_"," ")),"S","Objetivo analítico")
        ax.set_xlim(-.01,1.01)
    for ax in axs[len(cases):]:ax.axis("off")
    return finish(fig,"12_adversarial_gallery",
                  "Funciones analíticas del banco adversarial; no son necesariamente superficies de pérdida PLS.")


def sampling_density():
    res=find_stationary_points_smoothness(callback,n_obs=6,order=2)
    samples=np.asarray(res.sampled_smoothness_)
    fig,axs=canvas(1,2,title="13  |  Dónde concentra evaluaciones el muestreo adaptativo")
    axs[0].hist(samples,bins=50,range=(0,1),color=BLUE,alpha=.85)
    panel(axs[0],"Ubicaciones de evaluación","S","Evaluaciones por intervalo")
    for x in ROOT_S:axs[0].axvline(x,ls="--",color=ORANGE,alpha=.5)
    dist=np.diff(np.sort(samples))
    axs[1].semilogy((samples[1:]+samples[:-1])/2,np.maximum(dist,1e-15),".",color=PURPLE,ms=5)
    panel(axs[1],"Resolución espacial de las muestras finales","S","Separación entre valores de S (log)")
    return finish(fig,"13_adaptive_sampling_density",
                  f"Muestras finales reales del ejemplo de seis observaciones; n={len(samples)}. No representa la eficiencia en muestras grandes.")


FIGURES={
    "07_objective_derivative_curvature":derivative_profiles,
    "08_adaptive_search_steps":adaptive_steps,
    "09_endpoint_refinement_ablation":endpoint_failure,
    "10_sturm_worked_example":sturm_landscape,
    "11_lambda_vs_s_landscape":lambda_view,
    "12_adversarial_gallery":adversarial_gallery,
    "13_adaptive_sampling_density":sampling_density,
}
