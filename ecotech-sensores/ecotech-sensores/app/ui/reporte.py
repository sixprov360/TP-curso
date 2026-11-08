"""Impresión formateada del reporte final."""
from typing import Optional


def imprimir_reporte(
    sensores_alerta: list[str],
    promedio: Optional[float],
    umbral: float,
    total_registros: int,
) -> None:
    print("=" * 40)
    print("  REPORTE TÉRMICO - ECOTECH SOLUTIONS")
    print("=" * 40)
    print(f"Registros procesados : {total_registros}")
    print(f"Umbral de alerta     : {umbral:.1f} °C")
    if promedio is None:
        print("Promedio global      : sin datos válidos")
    else:
        print(f"Promedio global      : {promedio:.2f} °C")
    print(f"Sensores en alerta   : {len(sensores_alerta)}")
    for sensor_id in sensores_alerta:
        print(f"  - {sensor_id}")
    print("=" * 40)
