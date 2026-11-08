from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from sustentabilidad.datos_demo import REGISTROS_DEMO
from sustentabilidad.emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request: HttpRequest) -> HttpResponse:
    """Arma el contexto con las métricas y renderiza el panel administrativo."""
    metricas = obtener_metricas_consumo(REGISTROS_DEMO)

    contexto = {
        "titulo": "Panel de Sustentabilidad - EcoTech Solutions",
        "metricas": metricas,
    }
    return render(request, "sustentabilidad/panel.html", contexto)
