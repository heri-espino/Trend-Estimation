"""Applied figures exclusively from frozen, development/test-split CSV files."""
from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle

from _style import BLUE, ORANGE, GREEN, PURPLE, GREY, BLACK, COLORS
from _style import canvas, finish, panel, frozen_csv, annotate_kind


def _applied():
    return {
        "profiles":frozen_csv("applied","objective_profiles.csv"),
        "paths":frozen_csv("applied","applied_paths.csv"),
        "candidates":frozen_csv("applied","candidate_results.csv"),
        "cases":frozen_csv("applied","case_selection.csv"),
        "scan":frozen_csv("applied","configuration_scan.csv"),
    }


def case_panels(series: str, filename: str):
    data=_applied()
    profile=data["profiles"].loc[data["profiles"]["series"].eq(series)].sort_values("smoothness")
    candidates=data["candidates"].loc[data["candidates"]["series"].eq(series)].sort_values("cv_rank")
    paths=data["paths"].loc[data["paths"]["series"].eq(series)].copy()
    spec=data["cases"].loc[data["cases"]["series"].eq(series)].iloc[0]
    if profile.empty or candidates.empty or paths.empty:
        raise ValueError(f"Missing frozen applied case content for {series}")
    paths["date"]=pd.to_datetime(paths["date"])
    etiqueta = {"GDPC1":"PIB de EE. UU.","BTC-USD":"Bitcoin"}.get(series,series)
    fig,axs=canvas(1,3,title=f"{filename[:2]}  |  {etiqueta}: mínimos, tendencias estimadas y pronósticos distintos",height=7.0)

    ax=axs[0]
    ax.plot(profile["smoothness"],profile["cv_error"],color=BLUE,lw=2.3)
    for i,(_,cand) in enumerate(candidates.iterrows()):
        annotate_kind(ax,float(cand["smoothness"]),float(cand["cv_error"]),
                      f"CV-{int(cand['cv_rank'])}",COLORS[i])
    panel(ax,"CV de pronóstico calculada solo con desarrollo","S","ECM de CV")
    ax.set_xlim(-.025,1.025)

    ax=axs[1]
    train=paths.loc[paths["segment"].eq("train")]
    last_dates=np.sort(train["date"].unique())
    last_dates=last_dates[-min(80,len(last_dates)):]
    train=train.loc[train["date"].isin(last_dates)]
    observed=train.drop_duplicates("date").sort_values("date")
    ax.plot(observed["date"],observed["observed"],".",color=GREY,ms=4,alpha=.6,label="Observado")
    for i,(rank,part) in enumerate(train.groupby("cv_rank",sort=True)):
        ax.plot(part.sort_values("date")["date"],part.sort_values("date")["candidate_path"],
                lw=2.2,color=COLORS[i],label=f"CV-{int(rank)}: ajuste")
    panel(ax,"Ventana final de entrenamiento: ajustes","Fecha","Nivel observado")
    ax.legend(fontsize=9)
    ax.tick_params(axis="x",rotation=28)

    ax=axs[2]
    future=paths.loc[paths["segment"].eq("test")]
    observed=future.drop_duplicates("date").sort_values("date")
    ax.plot(observed["date"],observed["observed"],color=BLACK,marker="o",ms=3,lw=1.8,label="Observado (prueba reservada)")
    for i,(rank,part) in enumerate(future.groupby("cv_rank",sort=True)):
        p=part.sort_values("date")
        cand=candidates.loc[candidates["cv_rank"].eq(rank)].iloc[0]
        ax.plot(p["date"],p["candidate_path"],lw=2.1,color=COLORS[i],
                marker="." if len(p)<4 else None,
                label=f"CV-{int(rank)} / prueba-{int(cand['test_rank'])}")
    panel(ax,f"Pronósticos de candidatos fijados (h={int(spec['horizon'])})","Fecha","Nivel observado")
    ax.legend(fontsize=9)
    ax.tick_params(axis="x",rotation=28)
    fig.text(.02,.045,
             "La configuración y los candidatos se eligieron con desarrollo; las posiciones de prueba son retrospectivas.",
             fontsize=9,color=GREY)
    return finish(fig,filename,
                  "Resultados aplicados congelados de 2026-10-01; se muestran niveles, aunque los ECM se calcularon sobre logaritmos.")


def gdp_case():
    return case_panels("GDPC1","22_gdp_unimodal_contrast")


def spy_case():
    return case_panels("SPY","23_spy_rank_reversal")


def aapl_case():
    return case_panels("AAPL","24_aapl_separated_minima")


def btc_case():
    return case_panels("BTC-USD","25_btc_three_minima")


def candidate_rank_ratios():
    data=frozen_csv("applied","candidate_results.csv")
    show=data.loc[data["series"].isin(("SPY","BTC-USD"))].copy()
    fig,axs=canvas(1,2,title="26  |  El ganador de validación puede perder en prueba")
    for ax,series in zip(axs,("SPY","BTC-USD")):
        part=show.loc[show["series"].eq(series)].sort_values("cv_rank")
        ranks=np.arange(len(part))
        cv=part["cv_error"].to_numpy(float);test=part["test_mse"].to_numpy(float)
        width=.36
        ax.bar(ranks-width/2,cv/cv.min(),width,label="CV / mejor CV",color=BLUE)
        ax.bar(ranks+width/2,test/test.min(),width,label="Prueba / mejor prueba",color=ORANGE)
        ax.set_xticks(ranks,[f"CV-{int(v)}" for v in part["cv_rank"]])
        if max(np.max(cv/cv.min()),np.max(test/test.min()))>7:
            ax.set_yscale("log")
        panel(ax,f"{series} (clasificación de prueba solo diagnóstica)","Candidato según validación","ECM relativo")
        ax.legend(fontsize=9)
    return finish(fig,"26_validation_test_rank_comparison",
                  "Cocientes calculados solo con resultados congelados; el bloque de prueba no intervino en la selección.")


def multimodality_prevalence():
    scan=frozen_csv("applied","configuration_scan.csv")
    counts=scan.groupby("series").agg(
        total=("n_representative_candidates","size"),
        multimodal=("n_representative_candidates",lambda v: int((v>=2).sum())),
        three=("n_representative_candidates",lambda v: int((v>=3).sum())),
    ).reindex(["GDPC1","SPY","AAPL","BTC-USD"])
    fig,(ax,ax2)=canvas(1,2,title="27  |  La multimodalidad depende de los datos y la configuración")
    labs=["PIB" if x=="GDPC1" else "Bitcoin" if x=="BTC-USD" else x for x in counts.index]
    ax.bar(labs,counts["multimodal"],color=COLORS[:4])
    for i,(m,n) in enumerate(zip(counts["multimodal"],counts["total"])):
        ax.text(i,float(m)+.28,f"{m}/{n}",ha="center",fontsize=11)
    ax.set_ylim(0, max(12,int(counts["multimodal"].max())+3))
    panel(ax,"Configuraciones con al menos dos candidatos separados","","Cantidad")
    ax2.bar(labs,counts["three"],color=COLORS[:4])
    for i,m in enumerate(counts["three"]):
        ax2.text(i,float(m)+.12,str(m),ha="center",fontsize=11)
    ax2.set_ylim(0,max(5,int(counts["three"].max())+2))
    panel(ax2,"Configuraciones con al menos tres candidatos separados","","Cantidad")
    return finish(fig,"27_multimodality_by_asset",
                  "Exploración de desarrollo con 64 configuraciones por serie; no describe la frecuencia general en mercados financieros.")


def time_split():
    d=frozen_csv("applied","temporal_split_protocol.csv")
    cases=frozen_csv("applied","case_selection.csv")
    selected=cases.loc[cases["series"].eq("SPY")].iloc[0]
    rows=d.loc[
        (d["series"].eq("SPY")) &
        (d["order"].eq(selected["order"])) &
        (d["window"].eq(selected["window"])) &
        (d["horizon"].eq(selected["horizon"]))
    ].sort_values("split_number").tail(8)
    if rows.empty:raise ValueError("Missing SPY historical fold schedule")
    fig,(ax,ax2)=canvas(2,1,title="28  |  División temporal entre desarrollo y prueba: control de filtraciones",height=8.3)
    for k,(_,r) in enumerate(rows.iterrows()):
        t0=pd.Timestamp(r["train_start_date"])
        t1=pd.Timestamp(r["train_end_date"])
        v0=pd.Timestamp(r["validation_start_date"])
        v1=pd.Timestamp(r["validation_end_date"])
        ax.plot([t0,t1],[k,k],color=BLUE,lw=8,solid_capstyle="butt")
        ax.plot([v0,v1],[k,k],color=ORANGE,lw=8,solid_capstyle="butt")
    ax.axvline(pd.Timestamp(selected["development_end_date"]),color=BLACK,ls="--",lw=1.5)
    ax.set_yticks(np.arange(len(rows)),[f"Pliegue {int(v)}" for v in rows["split_number"]])
    ax.tick_params(axis="x",rotation=18)
    panel(ax,"Pliegues históricos completos: azul entrenamiento, naranja validación","Tiempo","")
    ax2.plot([pd.Timestamp(selected["development_start_date"]),pd.Timestamp(selected["development_end_date"])],
             [1,1],lw=16,solid_capstyle="butt",color=BLUE,label="Desarrollo")
    ax2.plot([pd.Timestamp(selected["test_start_date"]),pd.Timestamp(selected["test_end_date"])],
             [1,1],lw=16,solid_capstyle="butt",color=GREEN,label="Prueba reservada")
    ax2.set(ylim=(.1,1.8),yticks=[])
    ax2.legend(loc="upper center",ncol=2)
    ax2.tick_params(axis="x",rotation=18)
    panel(ax2,"El bloque de prueba se reserva antes de seleccionar","Tiempo","")
    return finish(fig,"28_actual_temporal_splits",
                  "Fechas del protocolo aplicado de SPY; solo visualización, sin redefinir divisiones.")


FIGURES={
    "22_gdp_unimodal_contrast":gdp_case,
    "23_spy_rank_reversal":spy_case,
    "24_aapl_separated_minima":aapl_case,
    "25_btc_three_minima":btc_case,
    "26_validation_test_rank_comparison":candidate_rank_ratios,
    "27_multimodality_by_asset":multimodality_prevalence,
    "28_actual_temporal_splits":time_split,
}
