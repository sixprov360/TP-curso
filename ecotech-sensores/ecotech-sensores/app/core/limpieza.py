"""Punto A: normalización de registros crudos de sensores."""
import re
from typing import Any, Optional

UBICACION_POR_DEFECTO = "Sin ubicación"


def _parsear_temperatura(valor: Any) -> Optional[float]:
    """Extrae el número de un texto como '24.5C' o '28,7 °C'.
    Devuelve None si no se puede interpretar."""
    if valor is None:
        return None
    if isinstance(valor, (int, float)):
        return float(valor)

    texto = str(valor).strip().replace(",", ".")
    coincidencia = re.search(r"-?\d+(?:\.\d+)?", texto)
    return float(coincidencia.group()) if coincidencia else None


def limpiar_registro_sensor(registro_raw: dict[str, Any]) -> dict[str, Any]:
    """Normaliza un registro crudo de sensor y devuelve un diccionario nuevo."""
    sensor_id = str(registro_raw.get("sensor_id", "")).strip()
    ubicacion = str(registro_raw.get("ubicacion") or "").strip()

    return {
        "sensor_id": sensor_id,
        "temperatura": _parsear_temperatura(registro_raw.get("temperatura")),
        "ubicacion": ubicacion or UBICACION_POR_DEFECTO,
    }
