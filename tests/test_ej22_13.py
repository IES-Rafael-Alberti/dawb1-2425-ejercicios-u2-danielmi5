import pytest
from src.ej22_13 import pedir_cadena, mostrar_eco, terminar_programa


def test_pedir_cadena(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "    b  u  ena s   ")
    assert pedir_cadena() == "buenas"
@pytest.mark.parametrize(
    "cadena, eco",
    [
        (["hola","adios", "salir"], "hola adios"),
        (["hola","buenos","días", "salir"], "hola buenos días"),
        (["g", "salir"],"g") 
    ]
)

def test_mostrar_eco(monkeypatch, cadena, eco):
    entrada = iter(cadena)
    monkeypatch.setattr('builtins.input', lambda _: next(entrada))
    assert mostrar_eco("") == eco
    
@pytest.mark.parametrize(
    "cadena, booleano",
    [
        ("salir", True),
        ("Hola", False),
        ("salida",False) 
    ]
)    
    
def test_terminar_programa (cadena, booleano):
    assert terminar_programa(cadena) == booleano