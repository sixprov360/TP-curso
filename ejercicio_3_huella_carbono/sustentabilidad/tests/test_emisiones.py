"""Punto A: auditoría del algoritmo de emisiones con unittest."""
import unittest

from sustentabilidad.emisiones import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):
    def test_calculo_nominal_con_factor_por_defecto(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(100), 40.0)

    def test_calculo_con_consumo_decimal(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(12.5), 5.0)

    def test_calculo_con_factor_personalizado(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(250, factor_emision=0.5), 125.0)

    def test_consumo_cero_es_valido_y_emite_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0), 0)

    def test_consumo_negativo_lanza_value_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-1)

    def test_consumo_negativo_con_factor_personalizado_tambien_lanza_error(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50, factor_emision=0.8)

    def test_mensaje_del_error_indica_el_valor_recibido(self):
        with self.assertRaises(ValueError) as contexto:
            calcular_emisiones_carbono(-7)
        self.assertIn("-7", str(contexto.exception))


if __name__ == "__main__":
    unittest.main()
