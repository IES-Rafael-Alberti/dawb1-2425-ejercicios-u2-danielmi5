import pytest 
from src.ej22_01 import pedir_cadena
# Código modificado para que pueda funcionar el test recibiendo datos

@pytest.mark.parametrize(
    "inpuqt, cadena",
    [
        ("hola","hola"),
        ("B u e n a     s  ","Buenas"), 
        ("Enci   clo  pe dia    ", "Enciclopedia")
    ]
)
def test_pedir_cadena(monkeypatch, inpuqt, cadena):
    monkeypatch.setattr('builtins.input', lambda __ : inpuqt)
    assert pedir_cadena() == cadena
    
