"""Pruebas de la capa de presentación en español del laboratorio Streamlit.

Las pruebas del código fuente no requieren dependencias opcionales. Las
pruebas de figuras se ejecutan al instalar .[dashboard].
"""
from __future__ import annotations

import ast
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest


APP_PATH = Path(__file__).resolve().parents[1] / "apps" / "smoothness_lab_advanced.py"


def test_aplicacion_tiene_sintaxis_python_valida():
    ast.parse(APP_PATH.read_text(encoding="utf-8"), filename=str(APP_PATH))


def test_titulos_secciones_y_etiquetas_formales_espanolas():
    source = APP_PATH.read_text(encoding="utf-8")
    for text in (
        "Laboratorio de suavizamiento de tendencias para pronósticos",
        "Tendencia y pronóstico",
        "Errores de validación 1",
        "Ramas y validación 2",
        "Matriz de suavizamiento",
        "Tablas y descargas",
        "ECM de validación 1",
        "ECM de validación 2",
        "Suavidad normalizada",
        "Grados de libertad efectivos",
        "Número de origen de validación",
        "índice de la observación",  # Leíble en la descripción del operador.
    ):
        assert text.lower() in source.lower(), text


@pytest.fixture(scope="module")
def ui():
    pytest.importorskip("plotly")
    pytest.importorskip("streamlit")
    import apps.smoothness_lab_advanced as app

    return app


def _resultado_ficticio():
    origenes = np.repeat([1, 2, 3], 4)
    s = np.tile(np.linspace(0, 1, 4), 3)
    superficies = pd.DataFrame({
        "origin": origenes,
        "smoothness": s,
        "val1_mse": np.array([3., 2., 4., 6.,
                              4., 1., 5., 8.,
                              5., 2., 4., 7.]),
    })
    ramas = pd.DataFrame({
        "origin": [1, 2, 3, 1, 2, 3],
        "branch_id": ["b1"] * 3 + ["b2"] * 3,
        "smoothness": [0.33, 0.34, 0.36, 0.66, np.nan, 0.64],
        "val2_mse": [1.2, 0.9, 0.8, 2.2, np.nan, 1.9],
    })
    return SimpleNamespace(
        surfaces=superficies,
        tracks=ramas,
        selected_branch="b1",
        final_surface=pd.DataFrame({
            "smoothness": [0., 0.33, 0.66, 1.],
            "val1_mse": [5., 2., 4., 8.],
        }),
        candidates=pd.DataFrame({
            "smoothness": [0.33],
            "val1_mse": [2.],
            "source": ["interior"],
        }),
        final_s=0.40,
        pooled_s=0.33,
        train_start=12,
        pretest_end=40,
        test_end=45,
        trend=np.linspace(10, 12, 28),
        pooled_trend=np.linspace(10, 11.9, 28),
        forecast=np.linspace(12, 12.3, 5),
        pooled_forecast=np.linspace(11.9, 12.1, 5),
    )


def test_diccionarios_conservan_identificadores_numericos(ui):
    from experiments.smoothness_cv.live_lab import RULES

    assert set(ui.REGLAS) == set(RULES)
    assert ui.MODOS["Rendimiento logarítmico"][0] == "Log return"
    assert ui.FRECUENCIAS["Semanal"] == "1wk"
    assert ui.RUIDOS["Normal (gaussiano)"] == "Gaussian"


def test_figura_serie_admite_indice_numerico_y_fechas(ui):
    result = _resultado_ficticio()
    for con_fechas in (False, True):
        frame = pd.DataFrame({
            "observed": 10 + 0.05 * np.arange(45),
        })
        if con_fechas:
            frame["date"] = pd.date_range("2024-01-01", periods=45)
        fig = ui._grafica_serie(
            frame, result, vista="forecast",
            unidad="Nivel de la variable (unidades originales)",
            order=2, manual_s=0.6, revelar_prueba=False,
            mostrar_agrupado=True, mostrar_latente=False,
            limitar_escala=False,
        )
        assert fig.layout.xaxis.title.text == (
            "Fecha" if con_fechas else "Número de observación"
        )
        assert "extrapolación" in fig.layout.title.text.lower()
        assert any("Pronóstico" in str(trace.name) for trace in fig.data)


def test_errores_muestran_ecm_absoluto_en_hover_aun_con_colores_relativos(ui):
    result = _resultado_ficticio()
    fig = ui._grafica_superficie(result, relativa=True)
    heatmap = fig.data[0]
    assert np.allclose(np.min(np.asarray(heatmap.z), axis=1), 1.0)
    assert np.allclose(np.asarray(heatmap.customdata), result.surfaces.pivot(
        index="origin", columns="smoothness", values="val1_mse"
    ).to_numpy())
    assert "ECM validación 1" in heatmap.hovertemplate
    assert fig.layout.xaxis.range == (0, 1)


def test_cronologia_separa_validaciones_y_prueba(ui):
    fig = ui._grafica_cronologia(
        90, ventana=28, horizonte=3, paso=5, reserva=5,
    )
    assert "Esquema cronológico" in fig.layout.title.text
    assert len(fig.data) == 7
    assert {trace.name for trace in fig.data} == {
        "Ajuste L", "Validación 1", "Validación 2", "Prueba",
    }
    prueba = next(trace for trace in fig.data if trace.name == "Prueba")
    assert prueba.base[0] == 85
    assert prueba.x[0] == 5
    assert prueba.y[0] == 1


def test_graficos_ramas_usen_ejes_y_etiquetas_en_espanol(ui):
    result = _resultado_ficticio()
    fig = ui._grafica_ramas(result, variable="val2_mse")
    assert "ECM de validación 2" in fig.layout.yaxis.title.text
    assert "Rama B1" in fig.data[0].name
    assert "seleccionada" in fig.data[0].name


def test_matriz_pesos_muestra_indices_y_no_confunde_con_matriz_ecm(ui):
    H = np.eye(4) * 0.7 + np.ones((4, 4)) * 0.075
    fig = ui._grafica_matriz(H, solo_magnitud=False)
    assert "Matriz de suavizamiento" in fig.layout.title.text
    assert "Observación de entrada j" in fig.data[0].hovertemplate
    assert np.allclose(fig.data[0].customdata, H)
    assert fig.layout.yaxis.autorange == "reversed"
