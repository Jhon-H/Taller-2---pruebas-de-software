"""Paquete de lógica de negocio de la calculadora."""

from .operations import sumar, restar, multiplicar, dividir, DivisionPorCeroError

__all__ = ["sumar", "restar", "multiplicar", "dividir", "DivisionPorCeroError"]
