"""
Pruebas de INTEGRACIÓN de la API Flask (capa de servicio).

A diferencia de test_operations.py (que prueba la lógica pura), estas
pruebas usan el test client de Flask para verificar que los endpoints
HTTP responden correctamente: código de estado, formato JSON y manejo
de errores (parámetros faltantes, no numéricos, división entre cero).

Estas pruebas también sirven como referencia de los casos que luego se
replican como pruebas de integración en SoapUI (ver carpeta /soapui) y
como escenarios E2E en Serenity BDD (ver carpeta /serenity).
"""

import pytest

from app import app


@pytest.fixture()
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200


# ---------------------------------------------------------------------------
# Suma
# ---------------------------------------------------------------------------

def test_api_sumar_positivos(client):
    resp = client.get("/sumar?a=5&b=3")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 8


def test_api_sumar_negativos(client):
    resp = client.get("/sumar?a=-5&b=-3")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == -8


# ---------------------------------------------------------------------------
# Resta
# ---------------------------------------------------------------------------

def test_api_restar_positivos(client):
    resp = client.get("/restar?a=10&b=4")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 6


def test_api_restar_negativos(client):
    resp = client.get("/restar?a=-10&b=-4")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == -6


# ---------------------------------------------------------------------------
# Multiplicación
# ---------------------------------------------------------------------------

def test_api_multiplicar_positivos(client):
    resp = client.get("/multiplicar?a=6&b=7")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 42


def test_api_multiplicar_negativos(client):
    resp = client.get("/multiplicar?a=-6&b=-7")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 42


# ---------------------------------------------------------------------------
# División
# ---------------------------------------------------------------------------

def test_api_dividir_positivos(client):
    resp = client.get("/dividir?a=20&b=5")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 4


def test_api_dividir_negativos(client):
    resp = client.get("/dividir?a=-20&b=-5")
    assert resp.status_code == 200
    assert resp.get_json()["resultado"] == 4


def test_api_dividir_por_cero(client):
    resp = client.get("/dividir?a=20&b=0")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


# ---------------------------------------------------------------------------
# Entradas inválidas
# ---------------------------------------------------------------------------

def test_api_parametros_faltantes(client):
    resp = client.get("/sumar?a=5")
    assert resp.status_code == 400


def test_api_parametros_no_numericos(client):
    resp = client.get("/sumar?a=cinco&b=3")
    assert resp.status_code == 400
