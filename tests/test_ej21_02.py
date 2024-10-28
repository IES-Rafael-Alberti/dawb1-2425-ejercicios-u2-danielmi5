import pytest 
from src.ej21_02 import comprobar_contraseña

@pytest.mark.parametrize(
    "contraseña, bool",
    [
        ("contraseña",True),
        ("CoNTrASEÑA",True), 
        ("22463", False)
    ]
)
def test_convertir_params(contraseña, bool):
    assert comprobar_contraseña(contraseña) == bool