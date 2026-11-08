import json

import pytest

from app.core.dispositivos import DispositivoEcologico, PanelSolar
from app.core.excepciones import StockInvalidoError
from app.data.gestor_inventario import GestorInventario


def test_stock_negativo_en_constructor():
    with pytest.raises(StockInvalidoError):
        DispositivoEcologico("X", 10.0, -1)


def test_stock_negativo_en_asignacion_no_modifica_el_valor():
    d = DispositivoEcologico("X", 10.0, 5)
    with pytest.raises(StockInvalidoError):
        d.stock = -3
    assert d.stock == 5


def test_stock_no_entero_es_invalido():
    d = DispositivoEcologico("X", 10.0, 5)
    with pytest.raises(StockInvalidoError):
        d.stock = "diez"


def test_stock_cero_es_valido():
    assert DispositivoEcologico("X", 10.0, 0).stock == 0


def test_panel_solar_hereda_y_personaliza_ficha():
    panel = PanelSolar("P", 100.0, 3, 450, 21.5)
    assert isinstance(panel, DispositivoEcologico)
    ficha = panel.ficha_tecnica()
    assert "450 W" in ficha and "21.5 %" in ficha and "3 unidades" in ficha


def test_guardar_catalogo_json(tmp_path):
    ruta = tmp_path / "catalogo.json"
    lista = [
        PanelSolar("Panel", 100.0, 3, 450, 21.5),
        DispositivoEcologico("Cargador", 20.0, 10),
    ]
    GestorInventario().guardar_catalogo_json(lista, str(ruta))
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    assert datos[0]["tipo"] == "PanelSolar" and datos[0]["potencia_watts"] == 450
    assert datos[1]["tipo"] == "DispositivoEcologico" and datos[1]["stock"] == 10
