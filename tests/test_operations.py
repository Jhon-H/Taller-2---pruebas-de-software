"""
Pruebas UNITARIAS (pytest) de la lógica de negocio pura.

Se prueba únicamente el módulo `calculadora.operations`, sin pasar por
Flask ni por la red. Cada operación se valida con números positivos,
negativos y casos límite (cero, división entre cero, tipos inválidos).
"""

import pytest

from calculadora.operations import sumar, restar, multiplicar, dividir, DivisionPorCeroError


# ---------------------------------------------------------------------------
# Suma
# ---------------------------------------------------------------------------

def test_sum_positive_numbers():
    assert sumar(5, 3) == 8


def test_sum_negative_numbers():
    assert sumar(-5, -3) == -8


def test_sum_with_zero():
    assert sumar(7, 0) == 7


# ---------------------------------------------------------------------------
# Resta
# ---------------------------------------------------------------------------

def test_subtract_positive_numbers():
    assert restar(10, 4) == 6


def test_subtract_negative_numbers():
    assert restar(-10, -4) == -6


def test_subtract_resulting_in_negative():
    assert restar(4, 10) == -6


# ---------------------------------------------------------------------------
# Multiplicación
# ---------------------------------------------------------------------------

def test_multiply_positive_numbers():
    assert multiplicar(6, 7) == 42


def test_multiply_negative_numbers():
    assert multiplicar(-6, -7) == 42


def test_multiply_positive_by_negative():
    assert multiplicar(6, -7) == -42


def test_multiply_by_zero():
    assert multiplicar(6, 0) == 0


# ---------------------------------------------------------------------------
# División
# ---------------------------------------------------------------------------

def test_divide_positive_numbers():
    assert dividir(20, 5) == 4


def test_divide_negative_numbers():
    assert dividir(-20, -5) == 4


def test_divide_positive_by_negative():
    assert dividir(20, -5) == -4


def test_divide_by_zero():
    with pytest.raises(DivisionPorCeroError):
        dividir(20, 0)


def test_divide_zero_by_number():
    assert dividir(0, 5) == 0


# ---------------------------------------------------------------------------
# Validación de tipos (caso límite adicional)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("operacion", [sumar, restar, multiplicar, dividir])
def test_operations_reject_non_numeric_input(operacion):
    with pytest.raises(TypeError):
        operacion("5", 3)
