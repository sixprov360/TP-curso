"""Excepciones propias del dominio de inventario."""


class StockInvalidoError(Exception):
    """Se lanza cuando se intenta asignar un stock inválido (negativo o no entero)."""
