import pytest 
from src.ej22_01 import pedir_cadena
# assert: comprueba si la salida de la función es == a la impuesta

@pytest.mark.parametrize(
    "inpuut, cadena",
    [
        ("hola","hola"),
        ("B u e n a     s  ","Buenas"), 
        ("Enci   clo  pe dia    ", "Enciclopedia")
    ]
)
def test_pedir_cadena(monkeypatch, input, cadena):
    # monkeypatch simula el input en la función pedir_cadena con variable "input"
    monkeypatch.setattr('builtins.input', lambda __ : input)
    assert pedir_cadena() == cadena
    
