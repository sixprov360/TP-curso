"""Lógica de negocio: cálculo de huella de carbono y métricas de consumo.

No depende de Django, así que se puede probar con `unittest` a secas.
"""
from typing import Any, Optional

FACTOR_EMISION_POR_DEFECTO = 0.4  # kg de CO2 por kWh (supuesto del enunciado)


def calcular_emisiones_carbono(
    consumo_kwh: float,
    factor_emision: float = FACTOR_EMISION_POR_DEFECTO,
) -> float:
    """Devuelve las emisiones asociadas a un consumo eléctrico.

    Raises:
        ValueError: si el consumo es negativo.
    """
    if consumo_kwh < 0:
        raise ValueError(f"El consumo no puede ser negativo (recibido: {consumo_kwh})")
    return consumo_kwh * factor_emision


def obtener_metricas_consumo(registros: list[dict[str, Any]]) -> dict[str, Any]:
    """Procesa el historial de consumos por planta.

    Cada registro tiene la forma {"planta": str, "consumo_kwh": float}. Una misma
    planta puede aparecer varias veces (historial): sus consumos se acumulan.

    Devuelve un diccionario con:
        total_emisiones_kg   -> emisiones globales de todas las plantas
        planta_mayor_consumo -> nombre de la planta que más consumió (None si no hay datos)
        consumo_mayor_kwh    -> consumo acumulado de esa planta
        detalle_plantas      -> lista por planta, ordenada de mayor a menor consumo

    Raises:
        ValueError: si algún registro tiene consumo negativo.
    """
    consumo_por_planta: dict[str, float] = {}
    emisiones_por_planta: dict[str, float] = {}

    for registro in registros:
        planta = registro["planta"]
        consumo = registro["consumo_kwh"]
        emisiones = calcular_emisiones_carbono(consumo)  # valida cada registro

        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0.0) + consumo
        emisiones_por_planta[planta] = emisiones_por_planta.get(planta, 0.0) + emisiones

    detalle_plantas = sorted(
        (
            {
                "planta": planta,
                "consumo_kwh": consumo_por_planta[planta],
                "emisiones_kg": emisiones_por_planta[planta],
            }
            for planta in consumo_por_planta
        ),
        key=lambda fila: fila["consumo_kwh"],
        reverse=True,
    )

    planta_mayor: Optional[str] = detalle_plantas[0]["planta"] if detalle_plantas else None
    consumo_mayor = detalle_plantas[0]["consumo_kwh"] if detalle_plantas else 0.0

    return {
        "total_emisiones_kg": sum(emisiones_por_planta.values()),
        "planta_mayor_consumo": planta_mayor,
        "consumo_mayor_kwh": consumo_mayor,
        "detalle_plantas": detalle_plantas,
    }
