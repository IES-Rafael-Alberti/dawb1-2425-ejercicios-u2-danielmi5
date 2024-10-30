import pytest 
from src.ej21_03 import comprobar_num, comprobar_division, es_decimal

@pytest.mark.parametrize(
    "num, booleano",
    [
        ("21", False),
        ("hola.dw", False), 
        ("11.454", True)
    ]
)
def test_es_decimal(num, booleano):
    assert es_decimal(num) == booleano


@pytest.mark.parametrize(
    "num, divisor, retorno",
    [
        (20, -4, -5.0),
        (10, 4, 2.5), 
        (11, 0, "*ERROR* --> No se puede dividir por 0")
    ]
)

def test_comprobar_division(num, divisor, retorno):
    assert comprobar_division(num, divisor) == retorno


@pytest.mark.parametrize(
    "num, retorno",
    [
        (["3.5"], 3.5),
        (["Hola","-start","-34"], -34), 
        (["11"], 11)
    ]
)

def test_comprobar_num(monkeypatch, num, retorno):
    entradas = iter(num)  # Crea un iterador de entradas
    monkeypatch.setattr('builtins.input', lambda _: next(entradas)) # el next lo que hace es q cambia a la prox variable
    assert comprobar_num("") == retorno


