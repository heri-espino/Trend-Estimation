"""Figures computed exclusively from tracked, fijado experiment CSVs."""
from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt

from _style import BLUE, ORANGE, GREEN, PURPLE, GREY, BLACK, COLORS
from _style import canvas, finish, panel, frozen_csv


def _benchmark_frames():
    return frozen_csv("synthetic","search_summary.csv"), frozen_csv("financial","search_summary.csv")


def selected_agreement():
    synth,financial=_benchmark_frames()
    fig,axs=canvas(1,2,title="14  |  Suavizamiento elegido: adaptativo frente a malla densa")
    for ax,(name,df),c in zip(axs,(("Sintético",synth),("Financiero",financial)),(BLUE,ORANGE)):
        ax.scatter(df["dense_best_s"],df["adaptive_best_s"],color=c,s=8,alpha=.28)
        ax.plot([0,1],[0,1],color=BLACK,ls="--",lw=1.2)
        panel(ax,f"{name} ({len(df):,} superficies)","S* de referencia densa","S* adaptativo")
        ax.set(xlim=(-.03,1.03),ylim=(-.03,1.03),aspect="equal")
    return finish(fig,"14_selected_s_agreement",
                  "Objetivos sintéticos y financieros congelados; la malla densa no certifica todas las raíces.")


def evaluation_cost():
    synthetic,financial=_benchmark_frames()
    adv=frozen_csv("adversarial","method_summary.csv")
    datasets=[
        ("Adversarial",adv.loc[adv["method"].eq("adaptive_s"),"n_evaluations"].to_numpy(float),
         adv.loc[adv["method"].eq("dense"),"n_evaluations"].to_numpy(float)),
        ("Sintético",synthetic["adaptive_evaluations"].to_numpy(float),
         synthetic["dense_evaluations"].to_numpy(float)),
        ("Financiero",financial["adaptive_evaluations"].to_numpy(float),
         financial["dense_evaluations"].to_numpy(float)),
    ]
    fig,(ax,ax2)=canvas(1,2,title="15  |  Costo en evaluaciones para las mismas superficies")
    for i,(name,adapt,dense) in enumerate(datasets):
        xpos=2*i+1
        ax.boxplot(adapt,positions=[xpos],widths=.58,patch_artist=True,
                   boxprops={"facecolor":BLUE,"alpha":.75},medianprops={"color":"white","linewidth":1.5},
                   showfliers=False)
        ax.scatter([xpos+.5],[np.median(dense)],marker="D",color=ORANGE,s=55,zorder=4)
    ax.set_xticks([1,3,5], [x[0] for x in datasets])
    ax.set_yscale("log")
    panel(ax,"Adaptativo (cajas); referencia densa (rombos)","","Evaluaciones (escala logarítmica)")
    names=[x[0] for x in datasets]
    fractions=[x[1].mean()/x[2].mean()*100 for x in datasets]
    ax2.bar(names,fractions,color=COLORS[:3],alpha=.86)
    for i,v in enumerate(fractions):ax2.text(i,v+.06,f"{v:.2f}%",ha="center",fontsize=11)
    panel(ax2,"Relación de evaluaciones promedio: adaptativo / denso","","Fracción de evaluaciones de la malla (%)")
    return finish(fig,"15_evaluation_efficiency",
                  "Cada evaluación adaptativa incluye la función y dos derivadas; el tiempo depende de la implementación.")


def error_ecdf():
    s,f=_benchmark_frames()
    fig,(ax,ax2)=canvas(1,2,title="16  |  Distribución de discrepancias numéricas")
    for label,df,color in (("Sintético",s,BLUE),("Financiero",f,ORANGE)):
        vals=np.sort(df["best_s_abs_error"].to_numpy(float))
        y=np.arange(1,len(vals)+1)/len(vals)
        ax.step(vals,y,where="post",lw=2.4,color=color,label=label)
        raw=df["objective_regret"].to_numpy(float)
        positive=np.maximum(raw,0)
        ax2.hist(np.log10(np.maximum(positive,1e-16)),bins=np.linspace(-16,-10,30),
                 histtype="step",lw=2,color=color,label=label)
    ax.legend(fontsize=10)
    panel(ax,"Distribución acumulada de |S* adaptativo - S* denso|","Discrepancia absoluta en S","Fracción acumulada")
    ax2.legend(fontsize=10)
    panel(ax2,"Arrepentimiento positivo (valores pequeños en -16)","log10(máx(arrepentimiento, 1e-16))","Cantidad de superficies")
    return finish(fig,"16_selection_error_distributions",
                  "Arrepentimiento respecto de mallas finitas; 1e-16 es solo el mínimo de la escala gráfica.")


def cost_by_order_horizon():
    s,_=_benchmark_frames()
    med=s.pivot_table(index="order",columns="horizon",values="adaptive_evaluations",aggfunc="median")
    fig,(ax,ax2)=canvas(1,2,title="17  |  Costo computacional según orden y horizonte")
    im=ax.imshow(med.to_numpy(),cmap="viridis",aspect="auto")
    ax.set_xticks(range(len(med.columns)),med.columns)
    ax.set_yticks(range(len(med.index)),med.index)
    ax.set(xlabel="Horizonte de pronóstico h",ylabel="Orden de diferencias d")
    ax.set_title("Mediana de evaluaciones adaptativas",loc="left")
    for i in range(len(med.index)):
        for j in range(len(med.columns)):
            ax.text(j,i,f"{med.iloc[i,j]:.0f}",ha="center",va="center",color="white",fontsize=12)
    fig.colorbar(im,ax=ax,fraction=.045,label="Evaluaciones")
    med2=s.pivot_table(index="order",columns="window",values="adaptive_evaluations",aggfunc="median")
    for d,c in zip(med2.index,COLORS):
        ax2.plot(med2.columns,med2.loc[d].to_numpy(float),"-o",lw=2,color=c,label=f"d={d}")
    ax2.legend(fontsize=9)
    panel(ax2,"Mediana de evaluaciones según longitud de ventana","L","Evaluaciones")
    return finish(fig,"17_cost_by_order_horizon_window",
                  "Cuadrícula sintética congelada de 1,920 superficies; medianas descriptivas, no cotas de complejidad.")


def sensitivity_tradeoff():
    dat=frozen_csv("sensitivity","sensitivity_summary.csv")
    fig,(ax,ax2)=canvas(1,2,title="18  |  Resultados del análisis de sensibilidad de un factor")
    primary=dat.loc[dat["is_primary"].astype(str).str.lower().eq("true")].iloc[0]
    for _,row in dat.iterrows():
        bad=int(row["missed_minima"])>0
        main=str(row["parameter"])=="primary"
        color=GREEN if main else (ORANGE if bad else BLUE)
        ax.scatter(row["mean_evaluations"],row["missed_minima"],s=120 if main else 45,color=color,zorder=4)
        if main or bad:
            ax.annotate("fijado" if main else f"{'refinamiento de extremos' if row['parameter'] == 'endpoint_refinement_levels' else row['parameter']}={row['setting']}",
                        (row["mean_evaluations"],row["missed_minima"]),
                        xytext=(6,8),textcoords="offset points",fontsize=9)
    panel(ax,"Costo frente a mínimos de referencia no detectados","Evaluaciones adaptativas promedio","Mínimos no detectados (216 superficies)")
    show=dat.loc[dat["parameter"].eq("endpoint_refinement_levels")].copy()
    show["levels"]=show["setting"].astype(int)
    show=show.sort_values("levels")
    ax2.plot(show["levels"],show["mean_evaluations"],"-o",color=BLUE,lw=2,label="Evaluaciones promedio")
    twin=ax2.twinx()
    twin.plot(show["levels"],show["missed_minima"],"-s",color=ORANGE,lw=2,label="Mínimos no detectados")
    panel(ax2,"Refinamiento de extremos: costo y recuperación","Niveles adicionales en los extremos","Evaluaciones promedio")
    twin.set_ylabel("Mínimos de malla densa no detectados")
    return finish(fig,"18_sensitivity_tradeoff",
                  "Sensibilidad de un factor por vez; no se reajustó el método principal después del experimento grande.")


def endpoint_frequencies():
    s,f=_benchmark_frames()
    fig,(ax,ax2)=canvas(1,2,title="19  |  Selección de puntos interiores y extremos exactos")
    for i,(name,df) in enumerate((("Sintético",s),("Financiero",f))):
        x=df["adaptive_best_s"].to_numpy(float)
        counts=[int(np.count_nonzero(x==0)),int(np.count_nonzero((x>0)&(x<1))),int(np.count_nonzero(x==1))]
        running=0
        for val,c,label in zip(counts,(ORANGE,BLUE,GREEN),("S = 0","Interior","S = 1")):
            ax.barh([name],[val],left=running,color=c,label=label if i==0 else "")
            if val:ax.text(running+val/2,name,str(val),ha="center",va="center",fontsize=10,color="white")
            running+=val
        ax2.hist(x,bins=np.linspace(0,1,26),alpha=.45,edgecolor="none",
                 label=name,color=BLUE if i==0 else ORANGE)
    ax.legend(ncol=3,loc="upper center",bbox_to_anchor=(.5,1.07),fontsize=9)
    panel(ax,"Ubicación del candidato global seleccionado","","Cantidad de superficies")
    ax2.legend(fontsize=10)
    panel(ax2,"Distribución del S* seleccionado","S* seleccionado","Frecuencia")
    return finish(fig,"19_exact_endpoint_frequencies",
                  "Conteos extraídos de resultados congelados; S=0 y S=1 son modelos exactos distintos.")


def adversarial_comparison():
    df=frozen_csv("adversarial","stationary_detection.csv")
    relevant=df.loc[~df["truth_kind"].eq("stationary_inflection")]
    labels=[("adaptive_s","Adaptativo en S"),("log_lambda","Búsqueda uniforme en log-lambda"),("dense","Referencia densa")]
    fig,(ax,ax2)=canvas(1,2,title="20  |  Recuperación de puntos conocidos en casos adversariales")
    for i,(key,name) in enumerate(labels):
        sub=relevant.loc[relevant["method"].eq(key)]
        detected=int(sub["detected"].astype(str).str.lower().eq("true").sum())
        total=len(sub)
        ax.barh([name],[detected],color=COLORS[i])
        ax.text(detected+1,name,f"{detected}/{total}",va="center")
    ax.set_xlim(0,270)
    ax.invert_yaxis()
    panel(ax,"Mínimos y extremos conocidos detectados","Puntos verdaderos detectados","")
    counts=df.loc[df["truth_kind"].eq("stationary_inflection")].groupby("method")["detected"].sum()
    for i,(key,name) in enumerate(labels):
        ax2.barh([name],[int(counts.get(key,0))],color=COLORS[i])
    ax2.invert_yaxis()
    panel(ax2,"Las inflexiones estacionarias no son el objetivo","Inflexiones estacionarias detectadas","")
    return finish(fig,"20_adversarial_method_comparison",
                  "Conteos del experimento adversarial; sus funciones analíticas no equivalen a la pérdida de PLS.")


def spacing_epsilon():
    df=frozen_csv("synthetic","candidate_sweep.csv")
    keys=["seed","scenario","order","window","horizon","epsilon"]
    # Each rank repeats counts for its surface and epsilon, so deduplicate before totals.
    one=df.drop_duplicates(subset=keys)
    agg=one.groupby("epsilon").agg(
        removed=("n_removed","sum"),
        available=("n_available_minima","sum"),
        surfaces=("rank","size"),
    ).sort_index()
    fig,(ax,ax2)=canvas(1,2,title="21  |  La separación épsilon resume los mínimos DESPUÉS de detectarlos")
    ax.plot(agg.index,agg["removed"],"-o",color=ORANGE,lw=2.6)
    panel(ax,"Candidatos secundarios suprimidos","Separación épsilon","Mínimos suprimidos")
    ax2.plot(agg.index,agg["available"]-agg["removed"],"-o",color=BLUE,lw=2.6,label="Conservados")
    ax2.plot(agg.index,agg["available"],"--",color=GREY,lw=1.7,label="Disponibles antes de separar")
    ax2.legend(fontsize=10)
    panel(ax2,"Candidatos conservados y disponibles","Separación épsilon","Número de candidatos")
    return finish(fig,"21_epsilon_candidate_spacing",
                  "Solo resumen: se conserva el mejor mínimo detectado. Se excluyen superficies sin candidatos interiores.")


FIGURES={
    "14_selected_s_agreement":selected_agreement,
    "15_evaluation_efficiency":evaluation_cost,
    "16_selection_error_distributions":error_ecdf,
    "17_cost_by_order_horizon_window":cost_by_order_horizon,
    "18_sensitivity_tradeoff":sensitivity_tradeoff,
    "19_exact_endpoint_frequencies":endpoint_frequencies,
    "20_adversarial_method_comparison":adversarial_comparison,
    "21_epsilon_candidate_spacing":spacing_epsilon,
}
