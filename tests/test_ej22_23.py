import pytest 
from src.ej22_23 import pedir_libro, comprobar_libro, contar_digitos_libro
# assert: comprueba si la salida de la función es == a la impuesta

def test_pedir_frase(monkeypatch):
    # monkeypatch simula el input en la función pedir_libro con esa cadena de prueba "Los 3 mosqueteros" de num
    monkeypatch.setattr('builtins.input', lambda _: "    Los 3 mosqueteros   ")
    assert pedir_libro() == "Los 3 mosqueteros"

@pytest.mark.parametrize(
    "libro, retorna",
    [
        ("hola", "hola"), 
        ("Los 3 mosqueteros", "Los 3 mosqueteros"), 
        ("*", None), 
    ]
)

def test_comprobar_libro(libro, retorna):
    assert comprobar_libro(libro) == retorna

@pytest.mark.parametrize(
    "libro, num_digitos",
    [
        ("La mañana", 0), 
        ("Los 3 mosqueteros", 1), 
        ("Las 3627481 cucarachas", 7), 
    ]
)

def test_contar_digitos_libro(libro, num_digitos):
    assert contar_digitos_libro(libro) == num_digitos
