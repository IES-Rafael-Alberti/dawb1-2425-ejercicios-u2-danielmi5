import pytest 
from src.ej22_11 import invertir_cadena, pedir_cadena
# Código modificado para que pueda funcionar el test recibiendo datos

@pytest.mark.parametrize(
    "input, cadena",
    [
        ("hola","hola"),
        ("B u e n a     s  ","Buenas"), 
        ("Enci   clo  pe dia    ", "Enciclopedia")
    ]
)
def test_pedir_cadena(monkeypatch,input, cadena):
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