"""
API REST de la calculadora, construida con Flask.

Expone cuatro endpoints, uno por operación. Todos reciben los
parámetros `a` y `b` por query string (para poder probarlos fácilmente
desde el navegador, curl, SoapUI o Serenity BDD) y devuelven un JSON
con el resultado.

Endpoints:
    GET /sumar?a=<num>&b=<num>
    GET /restar?a=<num>&b=<num>
    GET /multiplicar?a=<num>&b=<num>
    GET /dividir?a=<num>&b=<num>

Ejemplo de uso:
    GET /sumar?a=5&b=3        -> {"operacion": "suma", "a": 5.0, "b": 3.0, "resultado": 8.0}
    GET /dividir?a=20&b=0     -> 400 {"error": "No es posible dividir entre cero"}
"""

import os
from flask import Flask, jsonify, request

from calculadora.operations import (
    sumar,
    restar,
    multiplicar,
    dividir,
    DivisionPorCeroError,
)

app = Flask(__name__)


def _obtener_operandos():
    """Lee y valida los parámetros `a` y `b` de la query string.

    Retorna una tupla (a, b, error_response). Si hay un error de
    validación, a y b vienen en None y error_response contiene la
    respuesta JSON + código HTTP que debe devolverse de inmediato.
    """
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")

    if a_raw is None or b_raw is None:
        return None, None, (jsonify(error="Se requieren los parámetros 'a' y 'b'"), 400)

    try:
        a = float(a_raw)
        b = float(b_raw)
    except ValueError:
        return None, None, (jsonify(error="'a' y 'b' deben ser numéricos"), 400)

    return a, b, None


@app.route("/sumar", methods=["GET"])
def endpoint_sumar():
    a, b, error = _obtener_operandos()
    if error:
        return error
    resultado = sumar(a, b)
    return jsonify(operacion="suma", a=a, b=b, resultado=resultado)


@app.route("/restar", methods=["GET"])
def endpoint_restar():
    a, b, error = _obtener_operandos()
    if error:
        return error
    resultado = restar(a, b)
    return jsonify(operacion="resta", a=a, b=b, resultado=resultado)


@app.route("/multiplicar", methods=["GET"])
def endpoint_multiplicar():
    a, b, error = _obtener_operandos()
    if error:
        return error
    resultado = multiplicar(a, b)
    return jsonify(operacion="multiplicacion", a=a, b=b, resultado=resultado)


@app.route("/dividir", methods=["GET"])
def endpoint_dividir():
    a, b, error = _obtener_operandos()
    if error:
        return error
    try:
        resultado = dividir(a, b)
    except DivisionPorCeroError as exc:
        return jsonify(error=str(exc)), 400
    return jsonify(operacion="division", a=a, b=b, resultado=resultado)


@app.route("/", methods=["GET"])
def index():
    return jsonify(
        mensaje="API Calculadora - Taller 2 Diseño de Sistemas de Información",
        endpoints=["/sumar", "/restar", "/multiplicar", "/dividir"],
        ejemplo="/sumar?a=5&b=3",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5001)), debug=True)
