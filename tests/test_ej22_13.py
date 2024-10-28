import pytest
from src.ej22_13 import pedir_cadena, mostrar_eco, terminar_programa

@pytest.mark.parametrize(
    "cadena, retorno",
    [
        ("Hola", "Hola"),
        ( "B u  e   na s  ", "Buenas"),
        (" cham "," cham ") 
    ]
)

def test_pedir_cadena(monkeypatch, cadena, retorno):
    monkeypatch.setattr('builtins.input', lambda _: cadena)
    assert pedir_cadena() == retorno

@pytest.mark.parametrize(
    "cadena, eco",
    [
        ("a", "a"),
        ([" ","1","c"], "c"),
        ("g","g") 
    ]
)

def  test_mostrar_eco(cadena, eco)