import pytest 
from src.ej21_02 import comprobar_contraseña
# assert: comprueba si la salida de la función es == a la impuesta

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