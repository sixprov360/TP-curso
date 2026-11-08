from app.core.limpieza import limpiar_registro_sensor
from app.core.analisis import generar_resumen_sensores
from app.ui.reporte import imprimir_reporte

UMBRAL = 30.0

REGISTROS_CRUDOS = [
    {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
    {"sensor_id": "SENSOR-002", "temperatura": " 31.2 C ", "ubicacion": "Planta Sur"},
    {"sensor_id": " SENSOR-003", "temperatura": "28,7C"},  # sin ubicación
    {"sensor_id": "SENSOR-004 ", "temperatura": "35.0C", "ubicacion": ""},
    {"sensor_id": "SENSOR-005", "temperatura": "error", "ubicacion": "Planta Norte"},
]

if __name__ == "__main__":
    limpios = [limpiar_registro_sensor(r) for r in REGISTROS_CRUDOS]
    alertas, promedio = generar_resumen_sensores(limpios, UMBRAL)
    imprimir_reporte(alertas, promedio, UMBRAL, len(limpios))
