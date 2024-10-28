import pytest 
from src.ej22_12 import pedir_cadena, pedir_letra, comprobar_letra, contar_letra



def test_pedir_cadena(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Hola buenas")
    assert pedir_cadena() == "Hola buenas"

def test_pedir_letra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "a")
    assert pedir_letra() == "a"

@pytest.mark.parametrize(
    "letra, retorno",
    [
        ("a", "a"),
        ([" ","1","c"], "c"),
        ("g","g") 
    ]
)

def test_comprobar_letra(monkeypatch, letra, retorno):
    entradas = iter(letra)  # Crea un iterador de entradas
    monkeypatch.setattr('builtins.input', lambda _: next(entradas)) # el next lo que hace es q cambia a la prox variable
    resultado = comprobar_letra("")
    assert resultado == retorno

@pytest.mark.parametrize(
    "cadena, letra, num_letras",
    [
        ("Hola buenas tardes", "a", 3),
        ("Hola buenas tardes", "e", 2),
        ("Tres tristes tigres", "T", 4) 
    ]
)
def test_contar_letra(cadena, letra, num_letras):
    assert contar_letra(cadena, letra) == num_letras

