"""Punto B: monitoreo y mapeo estadístico de sensores."""
from typing import Any, Optional


def generar_resumen_sensores(
    lista_sensores_limpios: list[dict[str, Any]],
    umbral_temperatura: float,
) -> tuple[list[str], Optional[float]]:
    """Devuelve (IDs de sensores que superan el umbral, promedio global)."""
    sensores_alerta: list[str] = []
    temperaturas: list[float] = []

    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        if temp is None:  # lectura inválida: no entra en el promedio
            continue
        temperaturas.append(temp)
        if temp > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    promedio = sum(temperaturas) / len(temperaturas) if temperaturas else None
    return sensores_alerta, promedio
