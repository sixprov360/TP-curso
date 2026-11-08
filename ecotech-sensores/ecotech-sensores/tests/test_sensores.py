from app.core.limpieza import limpiar_registro_sensor, UBICACION_POR_DEFECTO
from app.core.analisis import generar_resumen_sensores


def test_limpia_id_y_temperatura():
    r = limpiar_registro_sensor(
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"}
    )
    assert r == {"sensor_id": "SENSOR-001", "temperatura": 24.5, "ubicacion": "Planta Norte"}


def test_ubicacion_por_defecto():
    r = limpiar_registro_sensor({"sensor_id": "S1", "temperatura": "20C"})
    assert r["ubicacion"] == UBICACION_POR_DEFECTO


def test_resumen_alertas_y_promedio():
    sensores = [
        {"sensor_id": "A", "temperatura": 20.0, "ubicacion": "x"},
        {"sensor_id": "B", "temperatura": 40.0, "ubicacion": "x"},
    ]
    alertas, promedio = generar_resumen_sensores(sensores, 30.0)
    assert alertas == ["B"]
    assert promedio == 30.0
