"""
Lógica de negocio de la calculadora.

Este módulo contiene únicamente las operaciones matemáticas puras,
separadas de la capa de API (ver app.py). Cada función:

- Recibe dos números (int o float).
- Valida el tipo de dato de entrada.
- Retorna el resultado numérico correspondiente.

La división maneja explícitamente el caso de división entre cero,
lanzando una excepción de dominio (DivisionPorCeroError) en vez de
dejar que Python lance el ZeroDivisionError genérico. Esto permite que
la capa de API traduzca el error a una respuesta HTTP controlada.
"""

from numbers import Number


class DivisionPorCeroError(Exception):
    """Se lanza cuando se intenta dividir entre cero."""


def _validar_numeros(a, b) -> None:
    """Valida que ambos parámetros sean numéricos (int o float).

    Se excluye bool explícitamente porque en Python bool es subclase
    de int, y no queremos aceptar True/False como números válidos.
    """
    for valor in (a, b):
        if isinstance(valor, bool) or not isinstance(valor, Number):
            raise TypeError(
                f"Se esperaba un número (int o float), se recibió: {type(valor).__name__}"
            )


def sumar(a, b):
    """Retorna la suma de a y b.

    Ejemplo:
        >>> sumar(5, 3)
        8
    """
    _validar_numeros(a, b)
    return a + b


def restar(a, b):
    """Retorna la diferencia entre a y b (a - b).

    Ejemplo:
        >>> restar(10, 4)
        6
    """
    _validar_numeros(a, b)
    return a - b


def multiplicar(a, b):
    """Retorna el producto de a y b.

    Ejemplo:
        >>> multiplicar(6, 7)
        42
    """
    _validar_numeros(a, b)
    return a * b


def dividir(a, b):
    """Retorna el cociente de a / b.

    Lanza DivisionPorCeroError si b es 0, en lugar de propagar el
    ZeroDivisionError nativo de Python, para dar un manejo de error
    explícito y propio del dominio de la aplicación.

    Ejemplo:
        >>> dividir(20, 5)
        4.0
    """
    _validar_numeros(a, b)
    if b == 0:
        raise DivisionPorCeroError("No es posible dividir entre cero")
    return a / b
