"""Punto B (parte 1): pruebas del procesamiento de métricas."""
import unittest

from sustentabilidad.emisiones import obtener_metricas_consumo


class TestObtenerMetricasConsumo(unittest.TestCase):
    def test_total_global_y_planta_de_mayor_consumo(self):
        registros = [
            {"planta": "A", "consumo_kwh": 100.0},
            {"planta": "B", "consumo_kwh": 300.0},
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertAlmostEqual(metricas["total_emisiones_kg"], 160.0)
        self.assertEqual(metricas["planta_mayor_consumo"], "B")
        self.assertAlmostEqual(metricas["consumo_mayor_kwh"], 300.0)

    def test_acumula_el_historial_de_una_misma_planta(self):
        registros = [
            {"planta": "A", "consumo_kwh": 100.0},
            {"planta": "B", "consumo_kwh": 150.0},
            {"planta": "A", "consumo_kwh": 100.0},  # A suma 200 y supera a B
        ]
        metricas = obtener_metricas_consumo(registros)
        self.assertEqual(metricas["planta_mayor_consumo"], "A")
        self.assertEqual(len(metricas["detalle_plantas"]), 2)

    def test_sin_registros(self):
        metricas = obtener_metricas_consumo([])
        self.assertEqual(metricas["total_emisiones_kg"], 0)
        self.assertIsNone(metricas["planta_mayor_consumo"])
        self.assertEqual(metricas["detalle_plantas"], [])

    def test_registro_con_consumo_negativo_propaga_value_error(self):
        with self.assertRaises(ValueError):
            obtener_metricas_consumo([{"planta": "A", "consumo_kwh": -10.0}])


if __name__ == "__main__":
    unittest.main()
