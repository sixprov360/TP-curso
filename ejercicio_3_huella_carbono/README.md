# EcoTech - Huella de Carbono

Auditoría del cálculo de emisiones con tests unitarios e integración en un panel web Django.

## Qué incluye

- `calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4)`: calcula emisiones; lanza `ValueError` ante consumo negativo.
- `obtener_metricas_consumo(registros)`: total global de emisiones y planta de mayor consumo a partir del historial.
- `vista_panel_sustentabilidad(request)`: vista Django que arma el contexto y renderiza `sustentabilidad/panel.html`.
- Tests con `unittest` (clase `TestCalculoEmisiones`) y pruebas de la vista con el cliente de test de Django.

## Estructura

`
config/                         # Settings y URLs del proyecto
sustentabilidad/
├── emisiones.py                # Lógica de negocio (sin Django)
├── datos_demo.py               # Registros de ejemplo
├── views.py                    # vista_panel_sustentabilidad
├── urls.py
├── templates/sustentabilidad/panel.html
└── tests/
    ├── test_emisiones.py       # TestCalculoEmisiones (Punto A)
    ├── test_metricas.py
    └── test_views.py
`

## Requisitos

Python 3.9 o superior.

## Instalación y uso

bash
python -m venv venv
venv\Scripts\activate        
pip install -r requirements.txt
python manage.py runserver


Abrir http://127.0.0.1:8000/sustentabilidad/panel/

## Tests

bash
python manage.py test
# Solo el Punto A, sin necesidad de Django:
python -m unittest sustentabilidad.tests.test_emisiones -v

