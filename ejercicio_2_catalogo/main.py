from app.core.dispositivos import DispositivoEcologico, PanelSolar
from app.core.excepciones import StockInvalidoError
from app.data.gestor_inventario import GestorInventario

RUTA_JSON = "catalogo_ecotech.json"


def main() -> None:
    catalogo: list[DispositivoEcologico] = []

    #1) Productos válidos 
    catalogo.append(PanelSolar("Panel Solar EcoMax 450W", 320000.0, 15, 450, 21.5))
    catalogo.append(DispositivoEcologico("Cargador solar portátil", 45000.0, 40))
    catalogo.append(PanelSolar("Panel Solar Compacto 200W", 150000.0, 8, 200, 19.8))

    #2) Intento de crear un producto con stock negativo 
    try:
        catalogo.append(PanelSolar("Panel Solar Defectuoso", 100000.0, -5, 300, 18.0))
    except StockInvalidoError as error:
        print(f"[Error capturado al crear] {error}")

    #3) Intento de modificar el stock de uno existente
    try:
        catalogo[0].stock = -1
    except StockInvalidoError as error:
        print(f"[Error capturado al asignar] {error}")
    print(f"Stock de '{catalogo[0].nombre}' sigue intacto: {catalogo[0].stock}\n")

    #4) Polimorfismo: misma llamada, ficha distinta según el tipo 
    for dispositivo in catalogo:
        print(dispositivo.ficha_tecnica())
        print("-" * 32)

    #5) Persistencia
    GestorInventario().guardar_catalogo_json(catalogo, RUTA_JSON)
    print(f"\nCatálogo exportado: {len(catalogo)} productos válidos en '{RUTA_JSON}'")


if __name__ == "__main__":
    main()
