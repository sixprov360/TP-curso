# EcoTech Catálogo

Módulo de gestión de productos ecológicos con validación de stock y persistencia en JSON.

## Qué incluye

- `StockInvalidoError`: excepción personalizada para stock inválido.
- `DispositivoEcologico`: clase base con el stock **encapsulado** (atributo privado + property con validación).
- `PanelSolar`: hereda de la base, suma potencia y eficiencia, y **sobrescribe** la ficha técnica (polimorfismo).
- `GestorInventario.guardar_catalogo_json(...)`: serializa el catálogo a `catalogo_ecotech.json`.

## Estructura

app/core/excepciones.py        # StockInvalidoError
app/core/dispositivos.py       # DispositivoEcologico y PanelSolar
app/data/gestor_inventario.py  # Persistencia JSON
main.py                        # Bloque de prueba completo
tests/                         # Pruebas con pytest


## Requisitos

Python 3.9 o superior.

## Instalación y uso

bash
python -m venv venv
venv\Scripts\activate        
pip install -r requirements.txt
python main.py


## Tests

bash
python -m pytest

