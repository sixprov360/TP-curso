"""Persistencia del catálogo en disco."""
import json
from pathlib import Path

from app.core.dispositivos import DispositivoEcologico


class GestorInventario:
    """Se encarga de guardar el catálogo; no sabe cómo se calcula ni se muestra."""

    def guardar_catalogo_json(
        self,
        lista_dispositivos: list[DispositivoEcologico],
        ruta_archivo: str,
    ) -> None:
        """Serializa los dispositivos y los escribe en `ruta_archivo` como JSON."""
        datos = [dispositivo.to_dict() for dispositivo in lista_dispositivos]
        ruta = Path(ruta_archivo)
        with ruta.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=2, ensure_ascii=False)
