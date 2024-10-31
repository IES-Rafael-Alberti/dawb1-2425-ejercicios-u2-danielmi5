import pytest 
from src.ej22_25 import pedir_frase, contar_num_palabras, encontrar_palabra_mas_larga
# assert: comprueba si la salida de la función es == a la impuesta

def test_pedir_frase(monkeypatch):
    # monkeypatch simula el input en la función pedir_frase con la cadena "hola buenas tardes"
    monkeypatch.setattr('builtins.input', lambda _: "   hola buenas tardes  ")
    assert pedir_frase() == "hola buenas tardes"

@pytest.mark.parametrize(
    "frase, num_palabras",
    [
        ("hola", 1), 
        ("   Hola  buenas      tardes", 3), 
        (" Tengo que irme a su casa", 6), 
    ]
)

def test_contar_num_palabras(frase, num_palabras):
    assert contar_num_palabras(frase) == num_palabras

@pytest.mark.parametrize(
    "frase, mas_larga",
    [
        ("hola", "hola"), 
        ("   Hola  buenas      tardes", "buenas"), 
        (" Tengo que irme a su casa", "Tengo"), 
    ]
)

def test_encontrar_palabra_mas_larga(frase, mas_larga):
    assert encontrar_palabra_mas_larga(frase) == mas_larga
