import pytest
from src.ej22_13 import pedir_cadena, mostrar_eco, terminar_programa
# assert: comprueba si la salida de la función es == a la impuesta

def test_pedir_cadena(monkeypatch):
    # monkeypatch simula el input en la función pedir_cadena con esa cadena. por ejemplo.
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
    entrada = iter(cadena)  # Crea un iterador de entradas
    # monkeypatch simula el input en la función comprobar_num con variable "entradas" de num
    monkeypatch.setattr('builtins.input', lambda _: next(entrada)) # el next lo que hace es q cambia a la prox variable
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