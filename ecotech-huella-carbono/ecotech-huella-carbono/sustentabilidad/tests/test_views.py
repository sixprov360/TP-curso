"""Punto B (parte 2): pruebas de la vista Django."""
from django.test import SimpleTestCase
from django.urls import reverse


class TestVistaPanelSustentabilidad(SimpleTestCase):
    def setUp(self):
        self.respuesta = self.client.get(reverse("sustentabilidad:panel"))

    def test_responde_200_y_usa_la_plantilla_correcta(self):
        self.assertEqual(self.respuesta.status_code, 200)
        self.assertTemplateUsed(self.respuesta, "sustentabilidad/panel.html")

    def test_el_contexto_trae_las_metricas(self):
        metricas = self.respuesta.context["metricas"]
        for clave in ("total_emisiones_kg", "planta_mayor_consumo", "detalle_plantas"):
            self.assertIn(clave, metricas)

    def test_la_planta_de_mayor_consumo_aparece_en_el_html(self):
        # En los datos demo, Planta Norte acumula 1200 + 1100 = 2300 kWh (la más alta)
        self.assertEqual(self.respuesta.context["metricas"]["planta_mayor_consumo"], "Planta Norte")
        self.assertContains(self.respuesta, "Planta Norte")
