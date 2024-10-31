import pytest 
from src.ej22_11 import invertir_cadena, pedir_cadena
# assert: comprueba si la salida de la función es == a la impuesta

@pytest.mark.parametrize(
    "input, cadena",
    [
        ("hola","hola"),
        ("B u e n a     s  ","Buenas"), 
        ("Enci   clo  pe dia    ", "Enciclopedia")
    ]
)
def test_pedir_cadena(monkeypatch,input, cadena):
    # monkeypatch simula el input en la función pedir_cadena con variable "input"
    monkeypatch.setattr('builtins.input', lambda __ : input)
    assert pedir_cadena() == cadena
    
@pytest.mark.parametrize(
    "cadena, cadena_invertida",
    [
        ("hola", "aloh"),
        ("Buenas", "saneuB"),
        ("Enciclopedia", "aidepolcicnE")
    ]
)
    
def test_invertir_cadena(cadena, cadena_invertida):
    assert invertir_cadena(cadena) == cadena_invertida