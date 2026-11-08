# EcoTech Sensores

Sanitización y análisis estadístico de lecturas térmicas de sensores.

## Qué hace

1. **Limpia** registros crudos (`limpiar_registro_sensor`): quita espacios del ID,
   convierte la temperatura a `float` sin unidades y asigna una ubicación por defecto.
2. **Analiza** los registros limpios (`generar_resumen_sensores`): devuelve los IDs
   que superan un umbral y el promedio térmico global.
3. **Reporta** el resultado por consola.

## Estructura


app/core/limpieza.py   # Punto A
app/core/analisis.py   # Punto B
app/ui/reporte.py      # Impresión del reporte
main.py                # Flujo completo de ejemplo
tests/                 # Pruebas con pytest


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


## Decisiones de diseño

- Una temperatura ilegible queda en `None` y se excluye del promedio.
- Si no hay lecturas válidas, el promedio es `None`.
- Se acepta coma decimal (`28,7C`).
