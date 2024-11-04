import pytest 
from src.ej24_01 import ordenar_lista, comprobar_lista_ordenada
# assert: comprueba si la salida de la función es == a la impuesta

@pytest.mark.parametrize(
    "lista, lista_ordenada",
    [
        ([8, 3, 1, 19, 14], [1, 3, 8, 14, 19]),
        ([45, 12, 4, 13, 23], [4, 12, 13, 23, 45]), 
    ]
)
def test_ordenar_lista(lista, lista_ordenada):
    assert ordenar_lista(lista) == lista_ordenada 

@pytest.mark.parametrize(
    "lista, booleano",
    [
        ([1, 3, 8, 14, 19], True),
        ([4, 12, 13, 23, 45], True),
        ([45, 12, 4, 13, 23], False), 
    ]
)
def test_comprobar_lista(lista, booleano):
    assert comprobar_lista_ordenada(lista) == booleano