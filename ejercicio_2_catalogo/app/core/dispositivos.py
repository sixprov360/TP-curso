"""Jerarquía de productos ecológicos del catálogo de EcoTech Solutions."""
from typing import Any

from app.core.excepciones import StockInvalidoError


class DispositivoEcologico:
    """Clase base de los productos del catálogo.

    El stock está encapsulado: el atributo real es privado (`__stock`) y solo
    se modifica a través de la property `stock`, que valida cada asignación.
    """

    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.stock = stock  # pasa por el setter: valida también al construir

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if isinstance(valor, bool) or not isinstance(valor, int):
            raise StockInvalidoError(
                f"El stock de '{self.nombre}' debe ser un entero, se recibió: {valor!r}"
            )
        if valor < 0:
            raise StockInvalidoError(
                f"El stock de '{self.nombre}' no puede ser negativo (recibido: {valor})"
            )
        self.__stock = valor

    def ficha_tecnica(self) -> str:
        """Ficha comercial genérica. Las subclases la personalizan (polimorfismo)."""
        return (
            f"Producto: {self.nombre}\n"
            f"Precio:   ${self.precio:,.2f}\n"
            f"Stock:    {self.stock} unidades"
        )

    def to_dict(self) -> dict[str, Any]:
        """Representación serializable (por ejemplo, a JSON)."""
        return {
            "tipo": type(self).__name__,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):
    """Panel solar: agrega potencia y eficiencia a los datos del producto base."""

    def __init__(
        self,
        nombre: str,
        precio: float,
        stock: int,
        potencia_watts: float,
        eficiencia: float,
    ) -> None:
        super().__init__(nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia  # porcentaje, por ejemplo 21.5

    def ficha_tecnica(self) -> str:
        """Sobrescribe la ficha base y le suma los datos propios del panel."""
        return (
            f"{super().ficha_tecnica()}\n"
            f"Potencia: {self.potencia_watts:g} W\n"
            f"Eficiencia: {self.eficiencia:g} %"
        )

    def to_dict(self) -> dict[str, Any]:
        datos = super().to_dict()
        datos["potencia_watts"] = self.potencia_watts
        datos["eficiencia"] = self.eficiencia
        return datos
